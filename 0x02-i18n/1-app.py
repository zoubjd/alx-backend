#!/usr/bin/env python3
"""multilingual and multi timezones Flask app"""
from flask import Flask, render_template
from flask_babel import Babel

babel = Babel()

app = Flask(__name__)


class Config():
    """Config class"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel.init_app(app)


@app.route('/')
def hello():
    """Return a HTML page"""
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(port=5000)
