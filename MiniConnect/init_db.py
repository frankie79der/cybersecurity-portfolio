import sqlite3
from werkzeug.security import generate_password_hash


connection = sqlite3.connect("miniconnect.db")

cursor = connection.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS friendships (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    friend_id INTEGER NOT NULL,
    status TEXT NOT NULL,
    UNIQUE(user_id, friend_id),
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (friend_id) REFERENCES users(id)
)
""")

users = [
    ("alice", generate_password_hash("alice123")),
    ("bob", generate_password_hash("bob123")),
    ("carlos", generate_password_hash("carlos123"))
]


cursor.executemany("""
INSERT OR IGNORE INTO users (username, password_hash)
VALUES (?, ?)
""", users)

bob = cursor.execute(
    "SELECT id FROM users WHERE username = ?",
    ("bob",)
).fetchone()

carlos = cursor.execute(
    "SELECT id FROM users WHERE username = ?",
    ("carlos",)
).fetchone()


cursor.execute("""
INSERT OR IGNORE INTO friendships (user_id, friend_id, status)
VALUES (?, ?, ?)
""", (bob[0], carlos[0], "accepted"))

connection.commit()
connection.close()


print("MiniConnect database initialized.")