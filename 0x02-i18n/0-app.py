#!/usr/bin/env python3
"""multilingual and multi timezones Flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """Return a HTML page"""
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run(port=5000)
