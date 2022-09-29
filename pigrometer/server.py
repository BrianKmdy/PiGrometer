from pigrometer.reader import Reader
import flask
import sqlite3
import json
import time
import os
from flask import request

app = flask.Flask(__name__)

def get_db():
    db = getattr(flask.g, '_database', None)
    if db is None:
        db = flask.g._database = sqlite3.connect(Reader.DATABASE)
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(flask.g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def home():
    return flask.render_template('chart.html',
        granularity=request.args.get('granularity', default=900, type=int),
        history=request.args.get('history', default=3, type=int))

@app.route('/data')
def data():
    granularity = request.args.get('granularity', type=int)
    history = request.args.get('history', type=int)

    response = json.dumps([row for row in get_db().cursor().execute(
        'SELECT * from humidity WHERE epoch % ? = 0 AND epoch > ?', (granularity, time.time() - (history * 24 * 60 * 60)))])
    return response

def run_server():
    app.run(host='0.0.0.0')

if __name__ == '__main__':
    run_server()