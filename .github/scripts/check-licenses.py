#!/usr/bin/env python3
"""
License checker script for GitHub Actions.

Usage: python3 check-licenses.py <json_file>

Where:
- json_file: Path to JSON file with license data

Supports three formats:
- Node (license-checker): {"pkg": {"licenses": "MIT", ...}}
- Python (pip-licenses): [{"Name": "pkg", "License": "MIT", ...}]
- CycloneDX SBOM: {"components": [{"name": "pkg", "licenses": [...]}]}
"""

import json
import sys
import re

def load_data(json_file):
    try:
        with open(json_file, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading {json_file}: {e}", file=sys.stderr)
        sys.exit(1)

def check_licenses(data, allowed):
    bad = []
    if isinstance(data, list):
        # Python format: list of dicts
        for item in data:
            name = item.get('Name')
            lic = item.get('License')
            if not license_allowed(lic, allowed):
                bad.append((name, lic))
    elif isinstance(data, dict):
        # Check for CycloneDX SBOM format
        if 'components' in data:
            for component in data['components']:
                name = component.get('name')
                lic_entries = component.get('licenses', [])
                # Extract license names/ids from nested structure
                lics = []
                for l in lic_entries:
                    if isinstance(l, dict):
                        lic_obj = l.get('license', {})
                        lic_id = lic_obj.get('id') or lic_obj.get('name')
                        if lic_id:
                            lics.append(lic_id)
                lic = lics[0] if len(lics) == 1 else lics if lics else None
                if not license_allowed(lic, allowed):
                    bad.append((name, lic))
        else:
            # Node format: dict of dicts
            for pkg, info in data.items():
                lic = info.get('licenses')
                if not license_allowed(lic, allowed):
                    bad.append((pkg, lic))
    else:
        print("Unknown JSON format", file=sys.stderr)
        sys.exit(1)
    return bad


def license_allowed(lic, allowed):
    """Return True if license value `lic` matches any allowed id.

    - `lic` can be None, a string, or a list/iterable.
    - `allowed` is a set of allowed identifiers (case-insensitive).
    """
    if lic == 'UNKNOWN':
        return True

    if lic is None:
        return False

    # Normalize allowed to lowercase tokens for substring matching
    allowed_lc = {a.lower() for a in allowed if a}

    # Normalize license value(s) to a list of strings
    if isinstance(lic, (list, tuple)):
        items = [str(x).lower() for x in lic if x]
    else:
        items = [str(lic).lower()]

    # For each item, build a token list and check any allowed token appears
    for item in items:
        s = item
        tokens = re.split(r"[^a-z0-9.-]+", s)
        if any(a in s or a in tokens for a in allowed_lc):
            return True
    return False

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 check-licenses.py <json_file>", file=sys.stderr)
        sys.exit(1)

    json_file = sys.argv[1]

    allowed = {
        'MIT',
        'Apache-2.0', 'Apache',
        'BSD-3-Clause', 'BSD-2-Clause', 'BSD',
        'ISC',
        'Python-2.0', 'Python',
        'LicenseRef-PolyForm-Shield-1.0.0', 'PolyForm', 'Shield'
    }

    data = load_data(json_file)
    bad = check_licenses(data, allowed)

    if bad:
        print('❌ Disallowed licenses found:')
        for name, lic in bad:
            print(f'  {name}: {lic}')
        sys.exit(1)
    else:
        print('✅ All licenses are allowed.')


if __name__ == '__main__':
    main()
