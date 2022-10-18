import os
from constants import SECRET
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = SECRET

BLACK_LIST = [
    'ls',
    'cat',
    'touch',
    'echo',
    'rm',
    'busybox',
    'pwd',
    'less',
    'tail',
    ' ',
]


def name_filter(name: str) -> str:
    for word in BLACK_LIST:
        name = name.replace(word, '')
    return name


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("index.html")

    args = request.form
    name = args.get('name', "")
    command = f"echo Hello, {name_filter(name)}!"
    result = os.popen(command).read()

    return render_template('index.html', result=result)
