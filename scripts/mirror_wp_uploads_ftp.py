#!/usr/bin/env python3
"""
Recursively download WordPress wp-content/uploads from FTP to a local folder.
Skips any file that already exists at the destination (same relative path).

Credentials: scripts/.ftp-credentials (gitignored) or FTP_HOST, FTP_USER, FTP_PASSWORD.
Optional: FTP_UPLOADS_ROOT (e.g. public_html/wp-content/uploads).

Usage:
  python scripts/mirror_wp_uploads_ftp.py [--dest "C:\\path\\to\\uploads"]
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

# Repo root (parent of scripts/)
SCRIPTS = Path(__file__).resolve().parent
ROOT = SCRIPTS.parent


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
            "Set FTP_HOST, FTP_USER, FTP_PASSWORD or create scripts/.ftp-credentials",
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


def find_remote_uploads_root(ftp):
    import ftplib

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
    ftp.cwd("/")
    for c in candidates:
        if try_cwd(c):
            return c
    raise SystemExit(
        "Could not find wp-content/uploads on FTP. Set FTP_UPLOADS_ROOT to the full path "
        "from FTP root (e.g. public_html/wp-content/uploads)."
    )


def ftp_cwd_abs(ftp, path_from_root: str):
    ftp.cwd("/")
    for seg in path_from_root.strip("/").split("/"):
        if seg:
            ftp.cwd(seg)


def list_entries(ftp):
    """Yield (name, is_dir) for current working directory."""
    try:
        for name, facts in ftp.mlsd():
            if name in (".", ".."):
                continue
            t = (facts.get("type") or "").lower()
            if t == "dir":
                yield name, True
            elif t == "file":
                yield name, False
            elif t == "cdir" or t == "pdir":
                continue
            else:
                yield name, None  # unknown
    except Exception:
        names = []
        ftp.retrlines("NLST", names.append)
        for name in names:
            if name in (".", ".."):
                continue
            yield name, None


def resolve_is_dir(ftp, name, unknown):
    if unknown is not None:
        return unknown
    pwd = ftp.pwd()
    try:
        ftp.cwd(name)
        ftp.cwd(pwd)
        return True
    except Exception:
        try:
            ftp.cwd(pwd)
        except Exception:
            pass
        return False


def mirror_tree(ftp, uploads_root: str, rel: str, dest: Path, stats: dict):
    import ftplib

    ftp_cwd_abs(ftp, uploads_root)
    if rel:
        for seg in rel.split("/"):
            if seg:
                ftp.cwd(seg)

    for name, kind in list_entries(ftp):
        remote_rel = f"{rel}/{name}" if rel else name
        local_path = dest / remote_rel.replace("/", os.sep)
        is_dir = resolve_is_dir(ftp, name, kind)
        if is_dir:
            local_path.mkdir(parents=True, exist_ok=True)
            pwd = ftp.pwd()
            mirror_tree(ftp, uploads_root, remote_rel, dest, stats)
            ftp.cwd(pwd)
        else:
            if local_path.exists():
                stats["skipped"] += 1
                continue
            local_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                with open(local_path, "wb") as out:
                    ftp.retrbinary("RETR " + name, out.write)
                stats["downloaded"] += 1
                if stats["downloaded"] % 200 == 0:
                    print("  ... %d files downloaded" % stats["downloaded"])
            except ftplib.error_perm as e:
                stats["failed"].append((remote_rel, str(e)))


def main():
    default_dest = r"C:\Users\JacobWorsøe\Dropbox\Arbejde\jacobworsoe.dk\Backup\uploads"
    ap = argparse.ArgumentParser(description="Mirror WordPress uploads from FTP; skip existing files.")
    ap.add_argument("--dest", default=default_dest, help="Local destination root")
    args = ap.parse_args()

    try:
        import ftplib
    except ImportError:
        raise SystemExit("ftplib is required")

    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)

    creds = load_ftp_creds()
    extra_root = os.environ.get("FTP_UPLOADS_ROOT", "").strip()

    print("Connecting FTP %s ..." % creds["host"])
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], timeout=120)
    ftp.login(creds["user"], creds["password"])
    ftp.set_pasv(True)

    if extra_root:
        ftp.cwd("/")
        try:
            ftp.cwd(extra_root)
            uploads_root = extra_root
        except Exception as e:
            raise SystemExit("FTP_UPLOADS_ROOT %r failed: %s" % (extra_root, e))
    else:
        uploads_root = find_remote_uploads_root(ftp)

    print("Remote uploads root: %s" % uploads_root)
    print("Local destination: %s" % dest)
    print("Mirroring (skip if file exists) ...")

    stats = {"downloaded": 0, "skipped": 0, "failed": []}
    mirror_tree(ftp, uploads_root, "", dest, stats)
    ftp.quit()

    print(
        "Done. Downloaded: %d, skipped (already exists): %d, failed: %d"
        % (stats["downloaded"], stats["skipped"], len(stats["failed"]))
    )
    if stats["failed"]:
        print("Failures (first 30):", file=sys.stderr)
        for r, e in stats["failed"][:30]:
            print(" ", r, e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
