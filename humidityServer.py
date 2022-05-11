import flask
import sqlite3
import datetime
import json

app = flask.Flask(__name__)

@app.route('/')
def home():
    return flask.render_template('index.html')

@app.route('/data')
def data():
    con = sqlite3.connect('humidity.db')
    response = json.dumps([row for row in con.cursor().execute('SELECT * from humidity')])
    con.close()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')