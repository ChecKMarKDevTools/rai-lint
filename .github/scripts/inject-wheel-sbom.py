#!/usr/bin/env python3
"""Inject an SBOM file into a wheel at:

  <distribution>.dist-info/sboms/bom.json

This updates RECORD appropriately.

Usage:
  inject-wheel-sbom.py --sbom /path/to/bom.json dist/*.whl
"""

from __future__ import annotations

import argparse
import base64
import csv
import hashlib
import io
import os
import sys
import tempfile
import zipfile


def _sha256_record_fields(data: bytes) -> tuple[str, str]:
    digest = hashlib.sha256(data).digest()
    b64 = base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")
    return f"sha256={b64}", str(len(data))


def _find_dist_info_dir(zf: zipfile.ZipFile) -> str:
    for name in zf.namelist():
        if name.endswith(".dist-info/WHEEL"):
            return name[: -len("WHEEL")].rstrip("/")
    raise RuntimeError("Could not locate *.dist-info/WHEEL in wheel")


def inject_sbom(wheel_path: str, sbom_path: str) -> None:
    with open(sbom_path, "rb") as f:
        sbom_bytes = f.read()

    with zipfile.ZipFile(wheel_path, "r") as zf:
        dist_info = _find_dist_info_dir(zf)
        record_path = f"{dist_info}/RECORD"
        sboms_dir = f"{dist_info}/sboms"
        sbom_inside = f"{sboms_dir}/bom.json"

        # Load existing RECORD (if missing, we'll create it)
        existing_record_rows: list[list[str]] = []
        if record_path in zf.namelist():
            with zf.open(record_path) as rf:
                text = rf.read().decode("utf-8")
            reader = csv.reader(io.StringIO(text))
            existing_record_rows = [row for row in reader if row]

        # Prepare new RECORD rows: keep everything except old RECORD and any old sbom entry.
        new_rows: list[list[str]] = []
        for row in existing_record_rows:
            if not row:
                continue
            path = row[0]
            if path in (record_path, sbom_inside):
                continue
            new_rows.append(row)

        sbom_hash, sbom_size = _sha256_record_fields(sbom_bytes)
        new_rows.append([sbom_inside, sbom_hash, sbom_size])
        # RECORD entry must have empty hash/size per wheel convention.
        new_rows.append([record_path, "", ""])

        record_buf = io.StringIO()
        writer = csv.writer(record_buf, lineterminator="\n")
        for row in new_rows:
            writer.writerow(row)
        record_bytes = record_buf.getvalue().encode("utf-8")

        # Rebuild wheel with injected sbom + updated RECORD.
        fd, tmp_path = tempfile.mkstemp(suffix=".whl")
        os.close(fd)
        try:
            with zipfile.ZipFile(tmp_path, "w") as out:
                for info in zf.infolist():
                    if info.filename in (record_path, sbom_inside):
                        continue
                    data = zf.read(info.filename)
                    out.writestr(info, data)

                # Ensure sboms directory entry is present (not strictly required, but nice).
                if not any(n == f"{sboms_dir}/" for n in out.namelist()):
                    out.writestr(f"{sboms_dir}/", b"")

                out.writestr(sbom_inside, sbom_bytes)
                out.writestr(record_path, record_bytes)

            os.replace(tmp_path, wheel_path)
        finally:
            try:
                os.remove(tmp_path)
            except FileNotFoundError:
                # If the temporary file was already removed elsewhere, there is nothing left to clean up.
                pass


def main(argv: list[str]) -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--sbom", required=True, help="Path to bom.json to inject")
    p.add_argument("wheels", nargs="+", help="Wheel path(s) to modify")
    args = p.parse_args(argv)

    sbom_path = args.sbom
    if not os.path.isfile(sbom_path):
        raise SystemExit(f"SBOM file not found: {sbom_path}")

    for wheel in args.wheels:
        if not os.path.isfile(wheel):
            raise SystemExit(f"Wheel not found: {wheel}")
        inject_sbom(wheel, sbom_path)

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
