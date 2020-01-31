import os

import pandas as pd
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

from flask import Flask, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')


@app.route("/line")
def test():
    data = [{
        "x": [1, 2, 3, 4, 5],
        "y": [1, 2, 4, 8, 16]}]

    return jsonify(data)


if __name__ == "__main__":
    app.run(debug=True)