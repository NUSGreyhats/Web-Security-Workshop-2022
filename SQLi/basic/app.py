from flask import Flask, flash, redirect, render_template, request, g
import sqlite3

from constants import USER_SETUP_QUERY, FLAG, INSERT_ADMIN_USER

app = Flask(__name__)
app.secret_key = "thisIsARandomSecretKey"


@app.before_first_request
def setup_db():
    db = sqlite3.connect("data.db")
    cursor = db.cursor()
    cursor.execute(USER_SETUP_QUERY).execute(INSERT_ADMIN_USER)
    db.commit()
    cursor.close()


@app.before_request
def make_cursor():
    g.db = sqlite3.connect("data.db")


@app.after_request
def close_db(response):
    g.db.close()
    return response


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["POST"])
def login():
    args = request.form
    username = args.get("username", None)
    password = args.get("password", None)

    if None in [username, password]:
        flash("Invalid username or password")
        return redirect("/")

    query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
    cursor = g.db.cursor()
    users = cursor.execute(query).fetchall()
    print(users)
    user = users[0] if len(users) > 0 else None

    if user is None:
        flash("Invalid username or password: " + query)
        return redirect("/")

    if user[0] == "admin":
        flash(FLAG)
        return redirect("/")
