import os
from flask import Flask, request, send_from_directory

BASE_DIRECTORY = os.path.dirname(os.path.abspath(__file__))
print(BASE_DIRECTORY)
FILE_DIRECTORY = 'files'
ABS_DIR = os.path.join(BASE_DIRECTORY, FILE_DIRECTORY)
print(ABS_DIR)

app = Flask(__name__)
app.secret_key = os.urandom(32)

@app.route('/', methods=['GET'])
def index():
    page = request.args.get('p', 'index.html')
    print(ABS_DIR)
    return send_from_directory(ABS_DIR, page)

@app.route('/<path:path>', methods=['GET'])
def get_file(path):
    return send_from_directory(ABS_DIR, path)