import os
import json
import sqlite3
from pathlib import Path
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = Path(__file__).parent / "career_compass.db"

SQL_PLACEHOLDER = "?"


def get_connection(database=None):
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        email TEXT UNIQUE,
        username TEXT UNIQUE,
        password_hash TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """)

    # Safe, idempotent migration for existing database schema
    cur.execute("PRAGMA table_info(users)")
    existing_cols = {row["name"] for row in cur.fetchall()}

    if "name" not in existing_cols:
        cur.execute("ALTER TABLE users ADD COLUMN name TEXT")
    if "email" not in existing_cols:
        cur.execute("ALTER TABLE users ADD COLUMN email TEXT")
    if "created_at" not in existing_cols:
        cur.execute("ALTER TABLE users ADD COLUMN created_at TIMESTAMP")
        cur.execute("UPDATE users SET created_at = CURRENT_TIMESTAMP WHERE created_at IS NULL")

    # Safe backfill for existing rows where email or name is NULL
    cur.execute("UPDATE users SET email = username WHERE email IS NULL AND username LIKE '%@%'")
    cur.execute("UPDATE users SET name = username WHERE name IS NULL")

    cur.execute("""
    CREATE TABLE IF NOT EXISTS survey_results (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        survey_type TEXT,
        data TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    """)

    cur.execute("""
    CREATE TABLE IF NOT EXISTS team_assignments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        domain TEXT NOT NULL,
        teammate_name TEXT NOT NULL,
        notes TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY(user_id) REFERENCES users(id)
    );
    """)

    conn.commit()
    conn.close()


def create_user(name: str, email: str, password: str):
    if not email or not password:
        raise ValueError("Email and password are required.")

    clean_email = email.strip().lower()
    clean_name = name.strip() if name else clean_email.split("@")[0]

    if not clean_email or "@" not in clean_email:
        raise ValueError("Please provide a valid email address.")

    if len(password) < 6:
        raise ValueError("Password must be at least 6 characters long.")

    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            f"INSERT INTO users (name, email, username, password_hash) VALUES ({SQL_PLACEHOLDER}, {SQL_PLACEHOLDER}, {SQL_PLACEHOLDER}, {SQL_PLACEHOLDER})",
            (clean_name, clean_email, clean_email, generate_password_hash(password))
        )
        conn.commit()
        user_id = cur.lastrowid
    except sqlite3.IntegrityError:
        conn.close()
        raise ValueError("An account with this email already exists.")
    except Exception:
        conn.close()
        raise

    conn.close()
    return user_id


def verify_user(email_or_username: str, password: str):
    if not email_or_username or not password:
        return None

    clean_identifier = email_or_username.strip()
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        f"SELECT id, name, email, username, password_hash, created_at FROM users WHERE LOWER(email) = LOWER({SQL_PLACEHOLDER}) OR LOWER(username) = LOWER({SQL_PLACEHOLDER})",
        (clean_identifier, clean_identifier)
    )
    row = cur.fetchone()
    conn.close()
    if not row:
        return None
    if check_password_hash(row["password_hash"], password):
        return {
            "id": row["id"],
            "name": row["name"] or row["username"],
            "email": row["email"] or row["username"],
            "username": row["username"],
            "created_at": row["created_at"]
        }
    return None


def get_user_by_id(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        f"SELECT id, name, email, username, created_at FROM users WHERE id = {SQL_PLACEHOLDER}",
        (user_id,)
    )
    row = cur.fetchone()
    conn.close()
    if not row:
        return None
    return dict(row)


def get_domain_assignments(user_id: int, domain: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        f"SELECT teammate_name, notes, created_at FROM team_assignments WHERE user_id = {SQL_PLACEHOLDER} AND domain = {SQL_PLACEHOLDER} ORDER BY created_at DESC",
        (user_id, domain)
    )
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def assign_teammate(user_id: int, domain: str, teammate_name: str, notes: str = None):
    if not teammate_name or not domain:
        raise ValueError("Domain and teammate name are required")
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO team_assignments (user_id, domain, teammate_name, notes) VALUES ({SQL_PLACEHOLDER}, {SQL_PLACEHOLDER}, {SQL_PLACEHOLDER}, {SQL_PLACEHOLDER})",
        (user_id, domain, teammate_name, notes)
    )
    conn.commit()
    conn.close()


def get_survey_results(user_id: int):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        f"SELECT id, survey_type, data, created_at FROM survey_results WHERE user_id = {SQL_PLACEHOLDER} ORDER BY created_at DESC",
        (user_id,)
    )
    rows = [dict(row) for row in cur.fetchall()]
    conn.close()
    return rows


def save_survey_result(user_id: int, survey_type: str, data: dict):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        f"INSERT INTO survey_results (user_id, survey_type, data) VALUES ({SQL_PLACEHOLDER}, {SQL_PLACEHOLDER}, {SQL_PLACEHOLDER})",
        (user_id, survey_type, json.dumps(data))
    )
    conn.commit()
    conn.close()


# Initialize DB on import if missing
try:
    init_db()
except Exception:
    pass
