#!/usr/bin/env python3
"""
Single entrypoint: export posts/pages (incl. settings + permalink) then comments.
Run from repo root: python scripts/export_all.py
"""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    scripts = ROOT / "scripts"
    steps = [
        [sys.executable, str(scripts / "export_wp_posts_pages_mysql.py")],
        [sys.executable, str(scripts / "export_wp_comments_mysql.py")],
    ]
    for cmd in steps:
        r = subprocess.run(cmd, cwd=str(ROOT))
        if r.returncode != 0:
            sys.exit(r.returncode)
    print("export_all: posts/pages + comments done.")


if __name__ == "__main__":
    main()
