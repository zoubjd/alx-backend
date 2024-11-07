#!/usr/bin/env python3
"""multilingual and multi timezones Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

babel = Babel()

app = Flask(__name__)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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
    if request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user():
    """Return a user dictionary or None"""
    login_as = request.args.get('login_as')
    if login_as:
        try:
            user_id = int(login_as)
            return users.get(user_id)
        except ValueError:
            return None
    return None


@app.before_request
def before_request():
    """sets the user if logged in"""
    g.user = get_user()


@app.route('/')
def hello():
    """Return a HTML page"""
    return render_template('5-index.html', user=g.user)


if __name__ == '__main__':
    app.run(port=5000)
