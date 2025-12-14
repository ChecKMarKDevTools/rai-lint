#!/usr/bin/env python3
"""
License checker script for GitHub Actions.

Usage: python3 check-licenses.py <json_file>

Where:
- json_file: Path to JSON file with license data

Supports two formats:
- Node (license-checker): {"pkg": {"licenses": "MIT", ...}}
- Python (pip-licenses): [{"Name": "pkg", "License": "MIT", ...}]
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

    allowed = {'MIT', 'Apache-2.0', 'BSD-3-Clause', 'BSD-2-Clause', 'ISC', 'Python-2.0', 'Polyform-Shield-1.0.0'}

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
