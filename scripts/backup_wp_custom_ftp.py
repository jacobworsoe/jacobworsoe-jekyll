#!/usr/bin/env python3
"""
Download WordPress files that are custom to your site (not core wp-admin/wp-includes).

Use with a fresh WordPress zip at restore time + your MySQL dump + wp-content/uploads backup.

Skips wp-content/uploads (mirror separately; e.g. mirror_wp_uploads_ftp.py → Backup\\uploads).
Skips regenerable dirs: upgrade, cache, common plugin log/cache folders.

Credentials: scripts/.ftp-credentials (gitignored) or FTP_HOST, FTP_USER, FTP_PASSWORD.
Optional: FTP_WEB_ROOT (e.g. public_html) if not auto-detected.

Usage:
  python scripts/backup_wp_custom_ftp.py
  python scripts/backup_wp_custom_ftp.py --dest "C:\\path\\to\\Backup\\wordpress-custom-restore"
"""
from __future__ import annotations

import argparse
import os
import sys
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parent

# Top-level wp-content subdirs to skip (uploads backed up elsewhere; rest regenerable or huge).
WP_CONTENT_SKIP_DIRS = frozenset(
    {
        "uploads",
        "upgrade",
        "cache",
        "wflogs",
        "et-cache",
        "ai1wm-backups",
        "backups",
        "updraft",
        "wc-logs",
        "nexus_performance",
        "bps-backup",
        "ithemes-security",
        "logs",
    }
)

ROOT_EXTRA_FILES = frozenset(
    {
        "robots.txt",
        "favicon.ico",
        ".user.ini",
        "php.ini",
    }
)


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


def find_web_root(ftp):
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

    ftp.cwd("/")
    for c in (
        "public_html",
        "httpdocs",
        "www",
        "htdocs",
        "domains/jacobworsoe.dk/public_html",
        "jacobworsoe.dk/public_html",
    ):
        if try_cwd(c):
            return c
    raise SystemExit(
        "Could not find web root (tried public_html, …). Set FTP_WEB_ROOT to the path from FTP /."
    )


def ftp_cwd_abs(ftp, path_from_root: str):
    ftp.cwd("/")
    for seg in path_from_root.strip("/").split("/"):
        if seg:
            ftp.cwd(seg)


def list_entries(ftp):
    try:
        for name, facts in ftp.mlsd():
            if name in (".", ".."):
                continue
            t = (facts.get("type") or "").lower()
            if t == "dir":
                yield name, True
            elif t == "file":
                yield name, False
            elif t in ("cdir", "pdir"):
                continue
            else:
                yield name, None
    except Exception:
        names = []
        ftp.retrlines("NLST", names.append)
        for name in names:
            if name not in (".", ".."):
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


def skip_wp_content_child(name: str, rel: str) -> bool:
    """Skip entire subtree if first segment under wp-content is excluded."""
    if rel:
        first = rel.split("/")[0].lower()
    else:
        first = name.lower()
    return first in WP_CONTENT_SKIP_DIRS


def mirror_wp_content(
    ftp,
    web_root: str,
    rel: str,
    dest_wp_content: Path,
    stats: dict,
):
    import ftplib

    ftp_cwd_abs(ftp, f"{web_root}/wp-content")
    if rel:
        for seg in rel.split("/"):
            if seg:
                ftp.cwd(seg)

    for name, kind in list_entries(ftp):
        remote_rel = f"{rel}/{name}" if rel else name
        if skip_wp_content_child(name, remote_rel):
            stats["skipped_dirs"] += 1
            continue
        local_path = dest_wp_content / remote_rel.replace("/", os.sep)
        is_dir = resolve_is_dir(ftp, name, kind)
        if is_dir:
            local_path.mkdir(parents=True, exist_ok=True)
            pwd = ftp.pwd()
            mirror_wp_content(ftp, web_root, remote_rel, dest_wp_content, stats)
            ftp.cwd(pwd)
        else:
            if name.lower() == "debug.log":
                stats["skipped_files"] += 1
                continue
            if local_path.exists():
                stats["skipped"] += 1
                continue
            local_path.parent.mkdir(parents=True, exist_ok=True)
            try:
                with open(local_path, "wb") as out:
                    ftp.retrbinary("RETR " + name, out.write)
                stats["downloaded"] += 1
                if stats["downloaded"] % 100 == 0:
                    print("  ... %d files" % stats["downloaded"])
            except ftplib.error_perm as e:
                stats["failed"].append((f"wp-content/{remote_rel}", str(e)))


def download_file_if_missing(
    ftp, web_root: str, remote_name: str, local_path: Path, stats: dict, *, optional: bool = False
):
    import ftplib

    if local_path.exists():
        stats["skipped"] += 1
        return
    ftp_cwd_abs(ftp, web_root)
    try:
        with open(local_path, "wb") as out:
            ftp.retrbinary("RETR " + remote_name, out.write)
        stats["downloaded"] += 1
        print("  OK %s" % remote_name)
    except ftplib.error_perm as e:
        if optional:
            print("  (skip, not on server) %s" % remote_name)
        else:
            stats["failed"].append((remote_name, str(e)))
            print("  FAIL %s — %s" % (remote_name, e))


def write_readme(dest: Path, web_root: str):
    text = f"""WordPress site-specific backup (FTP)
====================================

Web root on server: /{web_root}/

This folder is meant to sit beside your media backup, e.g.:
  ..\\uploads\\          ← wp-content/uploads (year/month/…)

Restore outline:
1. Install fresh WordPress from wordpress.org (same major version if possible).
2. Replace wp-config.php with the one here (edit DB_* to match your new DB), or merge
   unique lines (table prefix, salts, custom defines).
3. Copy .htaccess to the web root if you rely on permalinks / security rules.
4. Merge this wp-content/ over the new install (themes, plugins, mu-plugins, languages, …).
5. Restore wp-content/uploads from your uploads mirror (or copy into wp-content/uploads).
6. Import your MySQL dump.

Skipped on purpose: wp-content/uploads (use separate uploads backup), upgrade/, cache/,
and common log/backup plugin folders — see scripts/backup_wp_custom_ftp.py.

"""
    (dest / "RESTORE_NOTES.txt").write_text(text, encoding="utf-8")


def main():
    default_dest = (
        r"C:\Users\JacobWorsøe\Dropbox\Arbejde\jacobworsoe.dk\Backup\wordpress-custom-restore"
    )
    ap = argparse.ArgumentParser(description="FTP backup: custom WordPress files only.")
    ap.add_argument("--dest", default=default_dest, help="Local folder for this backup")
    args = ap.parse_args()

    try:
        import ftplib
    except ImportError:
        raise SystemExit("ftplib is required")

    dest = Path(args.dest)
    dest.mkdir(parents=True, exist_ok=True)
    wp_content_dest = dest / "wp-content"
    wp_content_dest.mkdir(parents=True, exist_ok=True)

    creds = load_ftp_creds()
    web_root = os.environ.get("FTP_WEB_ROOT", "").strip()

    print("Connecting FTP %s ..." % creds["host"])
    ftp = ftplib.FTP()
    ftp.connect(creds["host"], timeout=120)
    ftp.login(creds["user"], creds["password"])
    ftp.set_pasv(True)

    if web_root:
        ftp.cwd("/")
        try:
            ftp.cwd(web_root)
        except Exception as e:
            raise SystemExit("FTP_WEB_ROOT %r failed: %s" % (web_root, e))
    else:
        web_root = find_web_root(ftp)

    print("Web root: %s" % web_root)
    print("Destination: %s" % dest)

    stats = {
        "downloaded": 0,
        "skipped": 0,
        "skipped_dirs": 0,
        "skipped_files": 0,
        "failed": [],
    }

    print("Root files (.htaccess, wp-config.php, …) …")
    download_file_if_missing(ftp, web_root, ".htaccess", dest / ".htaccess", stats)
    download_file_if_missing(ftp, web_root, "wp-config.php", dest / "wp-config.php", stats)
    for extra in sorted(ROOT_EXTRA_FILES):
        download_file_if_missing(ftp, web_root, extra, dest / extra, stats, optional=True)

    # Apple touch icons often numbered
    ftp_cwd_abs(ftp, web_root)
    try:
        for name, kind in list_entries(ftp):
            if resolve_is_dir(ftp, name, kind):
                continue
            low = name.lower()
            if low.startswith("apple-touch-icon") and low.endswith(".png"):
                download_file_if_missing(ftp, web_root, name, dest / name, stats, optional=True)
    except Exception:
        pass

    print("wp-content/ (excluding uploads, upgrade, cache, …) …")
    mirror_wp_content(ftp, web_root, "", wp_content_dest, stats)

    write_readme(dest, web_root)
    ftp.quit()

    print(
        "Done. Downloaded: %d, skipped existing: %d, skipped dirs (uploads/cache/…): %d, "
        "skipped debug.log: %d, failed: %d"
        % (
            stats["downloaded"],
            stats["skipped"],
            stats["skipped_dirs"],
            stats["skipped_files"],
            len(stats["failed"]),
        )
    )
    if stats["failed"]:
        print("Failures (first 25):", file=sys.stderr)
        for r, e in stats["failed"][:25]:
            print(" ", r, e, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
