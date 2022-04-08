import os
from datetime import datetime

from flask import render_template

from api import app


@app.route('/api')
def api_home() -> str:
    return f"Hello from flask api! The environment is {os.environ['FLASK_ENV']}"


@app.route('/api/time', methods=['GET'])
def get_time() -> dict:
    return {'time': datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")}


@app.route('/')
def index():
    return app.send_static_file('index.html')
