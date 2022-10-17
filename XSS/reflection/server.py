from flask import Flask, render_template, request, redirect
from admin import visit
from urllib.parse import quote

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index() -> str:
    if request.method == "GET":
        # Get the Report arguments
        return render_template("index.html")

    args = request.form
    content = args.get("content", "")
    query_args = f"?content={quote(content)}"

    visit("http://rxss:2776", "http://rxss:2776" + query_args)
    return redirect(f"/{query_args}")
