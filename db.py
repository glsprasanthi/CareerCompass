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
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL
    );
    """)

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


def create_user(username: str, password: str):
    if not username or not password:
        raise ValueError("username and password required")
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(
            f"INSERT INTO users (username, password_hash) VALUES ({SQL_PLACEHOLDER}, {SQL_PLACEHOLDER})",
            (username, generate_password_hash(password))
        )
        conn.commit()
    except Exception as exc:
        conn.close()
        if isinstance(exc, sqlite3.IntegrityError):
            raise ValueError("username already exists")
        raise
    user_id = cur.lastrowid
    conn.close()
    return user_id


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


def verify_user(username: str, password: str):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(f"SELECT id, username, password_hash FROM users WHERE username = {SQL_PLACEHOLDER}", (username,))
    row = cur.fetchone()
    conn.close()
    if not row:
        return None
    if check_password_hash(row["password_hash"], password):
        return {"id": row["id"], "username": row["username"]}
    return None


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
