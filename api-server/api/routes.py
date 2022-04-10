"""
Empty module docstring
"""
import os
from datetime import datetime

from flask import render_template

from api import app


@app.route('/api')
def api_home() -> int:
    """
    Empty method docstring
    """

    return f"Hello from flask api! The environment is {os.environ['FLASK_ENV']}"


@app.route('/api/time', methods=['GET'])
def get_time() -> dict:
    """
    Empty method docstring
    """

    return {'time': datetime.utcnow().strftime("%m/%d/%Y, %H:%M:%S")}


@app.route('/')
def index():
    """
    Empty method docstring
    """

    return app.send_static_file('index.html')
