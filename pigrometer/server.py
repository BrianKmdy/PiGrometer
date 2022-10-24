import flask
import sqlite3
import time
from flask import request

from pigrometer import DB_PATH

app = flask.Flask(__name__)

# TODO/bmoody Move these into a default config file/structure
DEFAULT_GRANULARITY = 900
DEFAULT_HISTORY = 3


def get_db():
    db = getattr(flask.g, '_database', None)
    if db is None:
        db = flask.g._database = sqlite3.connect(DB_PATH)
    return db


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(flask.g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    return flask.render_template(
        'chart.html',
        granularity=request.args.get(
            'granularity', default=DEFAULT_GRANULARITY, type=int),
        history=request.args.get('history', default=DEFAULT_HISTORY, type=int))


@app.route('/data')
def data():
    granularity = request.args.get(
        'granularity', default=DEFAULT_GRANULARITY, type=int)
    history = request.args.get('history', default=DEFAULT_HISTORY, type=int)

    return flask.jsonify([row for row in get_db().cursor().execute(
        'SELECT * from humidity WHERE epoch % ? = 0 AND epoch > ?',
        (granularity, time.time() - (history * 24 * 60 * 60)))])


def run_server(port):
    app.run(host='0.0.0.0', port=port)


if __name__ == '__main__':
    run_server(5000)
