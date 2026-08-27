import sqlite3

from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import check_password_hash


app = Flask(__name__)
app.secret_key = "dev-secret-key"


def get_db_connection():
    connection = sqlite3.connect("miniconnect.db")
    connection.row_factory = sqlite3.Row
    return connection


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        connection = get_db_connection()

        user = connection.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        ).fetchone()

        connection.close()

        if user and check_password_hash(user["password_hash"], password):
            session["username"] = user["username"]
            session["user_id"] = user["id"]

            return redirect(url_for("dashboard"))

        return render_template(
            "login.html",
            error="Invalid username or password"
        )

    return render_template("login.html")


@app.route("/dashboard")
def dashboard():

    if "username" not in session:
        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        username=session["username"]
    )

@app.route("/users")
def users_list():

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()

    users = connection.execute(
        """
        SELECT id, username
        FROM users
        WHERE id != ?
        ORDER BY username
        """,
        (session["user_id"],)
    ).fetchall()

    connection.close()

    return render_template(
        "users.html",
        users=users,
        current_username=session["username"]
    )

@app.route("/logout")
def logout():

    session.clear()

    return redirect(url_for("login"))


@app.route("/profile/<int:user_id>")
def profile(user_id):

    if "user_id" not in session:
        return redirect(url_for("login"))

    connection = get_db_connection()

    user = connection.execute(
        """
        SELECT id, username
        FROM users
        WHERE id = ?
        """,
        (user_id,)
    ).fetchone()

    if user is None:
        connection.close()
        return "User not found", 404

    if user_id == session["user_id"]:
        connection.close()

        return render_template(
            "profile.html",
            user=user
        )

    friendship = connection.execute(
        """
        SELECT id
        FROM friendships
        WHERE status = 'accepted'
        AND (
            (user_id = ? AND friend_id = ?)
            OR
            (user_id = ? AND friend_id = ?)
        )
        """,
        (
            session["user_id"],
            user_id,
            user_id,
            session["user_id"]
        )
    ).fetchone()

    connection.close()

    if friendship is None:
        return "403 Forbidden - You are not friends with this user.", 403

    return render_template(
        "profile.html",
        user=user
    )

if __name__ == "__main__":
    app.run(debug=True)