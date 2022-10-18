import os
from constants import SECRET
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = SECRET

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    args = request.form
    name = args.get('name')
    result = os.popen(f"echo Hello, {name}!").read()

    return render_template('index.html', result=result)


