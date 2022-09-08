import flask
import sqlite3
import datetime
import json
import time

app = flask.Flask(__name__)

granularity = 180
history = 3 * 24 * 60 * 60

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/data')
def data():
    global granularity
    global history

    con = sqlite3.connect('humidity.db')
    response = json.dumps([row for row in con.cursor().execute('SELECT * from humidity WHERE epoch % ? = 0 AND epoch > ?', (granularity, time.time() - history))])
    con.close()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')
