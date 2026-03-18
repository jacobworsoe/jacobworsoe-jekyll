"""
Shared MySQL credentials for WordPress export scripts.
Reads scripts/.mysql-credentials (gitignored). Used by export_wp_posts_pages_mysql.py and export_wp_comments_mysql.py.
"""
from pathlib import Path


def load_credentials():
    cred_path = Path(__file__).resolve().parent / ".mysql-credentials"
    if not cred_path.exists():
        raise SystemExit(
            "Create scripts/.mysql-credentials with MySQL hostnavn, brugernavn, adgangskode, database."
        )
    lines = cred_path.read_text(encoding="utf-8").splitlines()
    creds = {}
    for line in lines:
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if ":" in line:
            key, _, val = line.partition(":")
            key = key.strip().lower().replace(" ", "_")
            val = val.strip()
            if key == "mysql_hostnavn":
                creds["host"] = val
            elif key == "mysql_port":
                creds["port"] = int(val) if val.isdigit() else 3306
            elif key == "mysql_brugernavn":
                creds["user"] = val
            elif key == "mysql_adgangskode":
                creds["password"] = val
            elif key == "primær_database" or (
                "database" in key and "primær" in key
            ):
                creds["database"] = val
    if not creds.get("host") or not creds.get("user") or not creds.get("password") or not creds.get("database"):
        raise SystemExit(
            ".mysql-credentials must contain MySQL hostnavn, brugernavn, adgangskode, Primær database."
        )
    creds.setdefault("port", 3306)
    return creds
