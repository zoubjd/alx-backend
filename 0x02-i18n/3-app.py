#!/usr/bin/env python3
"""multilingual and multi timezones Flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel

babel = Babel()

app = Flask(__name__)


class Config():
    """Class for config"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel.init_app(app)


@babel.localeselector
def get_locale():
    """Return the best match language"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def hello():
    """Return a HTML page"""
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(port=5000)
