import sqlite3
import hashlib
from pathlib import Path


DB_FILE = Path(__file__).with_name("users.db")


def get_connection():
    return sqlite3.connect(DB_FILE)


def initialize_database():
    with get_connection() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL
            )
        """)

        connection.commit()


def hash_password(password):
    return hashlib.sha256(
        password.encode("utf-8")
    ).hexdigest()


def create_user(username, email, password):

    try:
        with get_connection() as connection:

            connection.execute(
                """
                INSERT INTO users
                (username, email, password)
                VALUES (?, ?, ?)
                """,
                (
                    username,
                    email,
                    hash_password(password)
                )
            )

            connection.commit()

        return True, "Account created successfully."

    except sqlite3.IntegrityError:
        return False, "Username or email already exists."


def authenticate_user(username, password):

    with get_connection() as connection:

        user = connection.execute(
            """
            SELECT id
            FROM users
            WHERE username = ?
            AND password = ?
            """,
            (
                username,
                hash_password(password)
            )
        ).fetchone()

    return user is not None


def reset_password(username, email, new_password):

    with get_connection() as connection:

        user = connection.execute(
            """
            SELECT id
            FROM users
            WHERE username = ?
            AND email = ?
            """,
            (
                username,
                email
            )
        ).fetchone()

        if not user:
            return False, "Username and email do not match."

        connection.execute(
            """
            UPDATE users
            SET password = ?
            WHERE id = ?
            """,
            (
                hash_password(new_password),
                user[0]
            )
        )

        connection.commit()

    return True, "Password reset successfully."


initialize_database()