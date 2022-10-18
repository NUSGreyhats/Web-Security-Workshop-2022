from flask import Flask, render_template, request, g
from constants import SECRET
import sqlite3

app = Flask(__name__)
app.secret_key = SECRET


@app.before_request
def make_cursor():
    g.db = sqlite3.connect('database.db')
    g.cursor = g.db.cursor()


@app.after_request
def close_db(response):
    g.cursor.close()
    g.db.close()
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    company = request.form.get("company", "")
    query = f"SELECT * FROM companies WHERE name like '%{company}%';"
    companies = g.cursor.execute(query).fetchall()
    return render_template("index.html", companies=companies)
