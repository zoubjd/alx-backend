#!/usr/bin/env python3
"""multilingual and multi timezones Flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
import pytz
from babel import dates
from datetime import datetime

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
    elif g.user:
        if g.user.get('locale') in app.config['LANGUAGES']:
            return g.user.get('locale')
        else:
            return request.accept_languages.best_match(app.config['LANGUAGES'])
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@babel.timezoneselector
def get_timezone():
    """Return the best match timezone"""
    try:
        if request.args.get('timezone'):
            return pytz.timezone(request.args.get('timezone'))
        elif g.user:
            return pytz.timezone(g.user.get('timezone'))
        else:
            return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])
    except pytz.UnknownTimeZoneError:
        # Fallback to default timezone if an invalid timezone is provided
        return pytz.timezone(app.config['BABEL_DEFAULT_TIMEZONE'])


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
    """Return an HTML page"""
    timezone = get_timezone()
    locale = get_locale()  # get the selected locale
    dt = datetime.now(tz=timezone)  # use the timezone for accurate currenttime
    time = dates.format_datetime(dt, locale=locale)  # use locale in formatting
    return render_template('index.html', user=g.user, time=time)


if __name__ == '__main__':
    app.run(port=5000)
