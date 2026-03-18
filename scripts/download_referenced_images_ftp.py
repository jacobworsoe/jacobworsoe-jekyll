#!/usr/bin/env python3
"""
Find all /assets/images/... paths referenced in the Jekyll repo, download each from FTP
(wp-content/uploads/...) into assets/images/..., then print summary.
Credentials: scripts/.ftp-credentials (gitignored) or env FTP_HOST, FTP_USER, FTP_PASSWORD.

Run from repo root: python scripts/download_referenced_images_ftp.py
Optional: --favicon copies public_html/favicon.ico into assets/images/.
"""
import argparse
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = Path(__file__).resolve().parent

REF_PATTERN = re.compile(r"/assets/images/([^'\"|>\s]+)")


def load_ftp_creds():
    env = {
        "host": os.environ.get("FTP_HOST", "").strip(),
        "user": os.environ.get("FTP_USER", "").strip(),
        "password": os.environ.get("FTP_PASSWORD", "").strip(),
    }
    if env["host"] and env["user"] and env["password"]:
        return env
    p = SCRIPTS / ".ftp-credentials"
    if not p.exists():
        print(
            "Set FTP_HOST, FTP_USER, FTP_PASSWORD or create scripts/.ftp-credentials:\n"
            "  FTP host: linux12.unoeuro.com\n"
            "  FTP user: ...\n"
            "  FTP password: ...",
            file=sys.stderr,
        )
        sys.exit(1)
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            k, _, v = line.partition(":")
            k = k.strip().lower().replace(" ", "_")
            v = v.strip()
            if "host" in k:
                env["host"] = v
            elif "user" in k or "bruger" in k:
                env["user"] = v
            elif "pass" in k or "adgang" in k:
                env["password"] = v
    if not env["host"] or not env["user"] or not env["password"]:
        raise SystemExit("scripts/.ftp-credentials needs host, user, password")
    return env


def collect_referenced_paths():
    paths = set()
    files = []
    files.extend((ROOT / "_posts").glob("*.md"))
    files.extend(ROOT.glob("*.md"))
    files.extend((ROOT / "_includes").glob("*.html"))
    for f in files:
        try:
            text = f.read_text(encoding="utf-8")
        except OSError:
            continue
        for m in REF_PATTERN.finditer(text):
            rel = m.group(1).strip().rstrip("/")
            if rel and not rel.startswith(".."):
                paths.add(rel)
    return sorted(paths)


def find_remote_uploads_root(ftp):
    import ftplib

    ftp.cwd("/")
    tried = []

    def try_cwd(path):
        try:
            ftp.cwd(path)
            return True
        except ftplib.error_perm:
            try:
                ftp.cwd("/")
            except Exception:
                pass
            return False

    candidates = [
        "wp-content/uploads",
        "public_html/wp-content/uploads",
        "httpdocs/wp-content/uploads",
        "www/wp-content/uploads",
        "htdocs/wp-content/uploads",
        "domains/jacobworsoe.dk/public_html/wp-content/uploads",
        "jacobworsoe.dk/public_html/wp-content/uploads",
    ]
    for c in candidates:
        if try_cwd(c):
            return c
    # BFS from root for wp-content/uploads
    def list_names(path):
        names = []
        try:
            ftp.cwd(path)
            ftp.retrlines("NLST", names.append)
        except Exception:
            pass
        try:
            ftp.cwd("/")
        except Exception:
            pass
        return names

    for name in list_names("/"):
        if name in (".", ".."):
            continue
        sub = name + "/wp-content/uploads"
        if try_cwd(sub):
            return sub
        sub2 = name + "/public_html/wp-content/uploads"
        if try_cwd(sub2):
            return sub2
    raise SystemExit(
        "Could not find wp-content/uploads on FTP. List root with an FTP client and set "
        "FTP_UPLOADS_ROOT in .ftp-credentials (e.g. FTP uploads root: public_html/wp-content/uploads)"
    )


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "--favicon",
        action="store_true",
        help="Download public_html/favicon.ico to assets/images/favicon.ico",
    )
    args = ap.parse_args()

    try:
        import ftplib
    except ImportError:
        raise SystemExit("ftplib is stdlib")

    rel_paths = collect_referenced_paths()
    if not rel_paths:
        print("No /assets/images/ references found.")
        return 0

    creds = load_ftp_creds()
    extra_root = os.environ.get("FTP_UPLOADS_ROOT", "").strip()
    out_base = ROOT / "assets" / "images"

    print("Connecting FTP %s ..." % creds["host"])
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], timeout=60)
    ftp.login(creds["user"], creds["password"])
    ftp.set_pasv(True)

    if extra_root:
        try:
            ftp.cwd("/")
            ftp.cwd(extra_root)
            remote_uploads = extra_root
        except Exception as e:
            raise SystemExit("FTP_UPLOADS_ROOT %r failed: %s" % (extra_root, e))
    else:
        remote_uploads = find_remote_uploads_root(ftp)

    print("Remote uploads root: %s" % remote_uploads)
    print("Downloading %d referenced files to assets/images/ ..." % len(rel_paths))

    ok, fail = 0, []
    for rel in rel_paths:
        remote = rel.replace("\\", "/")
        local = out_base / remote
        local.parent.mkdir(parents=True, exist_ok=True)
        try:
            with open(local, "wb") as out:
                ftp.retrbinary("RETR " + remote, out.write)
            ok += 1
            print("  OK", rel)
        except Exception as e:
            fail.append((rel, str(e)))
            print("  FAIL", rel, e)

    if args.favicon:
        try:
            ftp.cwd("/")
            ftp.cwd("public_html")
            fav = out_base / "favicon.ico"
            fav.parent.mkdir(parents=True, exist_ok=True)
            with open(fav, "wb") as out:
                ftp.retrbinary("RETR favicon.ico", out.write)
            print("  OK favicon.ico -> assets/images/")
        except Exception as e:
            print("  FAIL favicon.ico", e)

    ftp.quit()
    print("Downloaded %d/%d." % (ok, len(rel_paths)))
    if fail:
        print("Failures (try FTP_UPLOADS_ROOT or check path):", file=sys.stderr)
        for r, e in fail[:20]:
            print(" ", r, e, file=sys.stderr)

    return 0 if not fail else 1


if __name__ == "__main__":
    sys.exit(main() or 0)
