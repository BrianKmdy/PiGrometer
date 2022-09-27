import flask
import sqlite3
import json
import time
import os
import threading
from flask import request

app = flask.Flask(__name__)

@app.route('/')
def home():
    granularity = request.args.get('granularity', default=900, type=int)
    history = request.args.get('history', default=(3 * 24 * 60 * 60), type=int)

    return flask.render_template('chart.html', granularity=granularity, history=history)

@app.route('/data')
def data():
    granularity = request.args.get('granularity', type=int)
    history = request.args.get('history', type=int)

    con = sqlite3.connect(os.path.join(os.path.expanduser("~"), '.pigrometer', 'pigrometer.db'))
    response = json.dumps([row for row in con.cursor().execute('SELECT * from humidity WHERE epoch % ? = 0 AND epoch > ?', (granularity, time.time() - history))])
    con.close()
    return response

# class Server(threading.Thread):
#     def __init__(self):
#         super().__init__()
#         self.terminate = threading.Event()

    

    

if __name__ == '__main__':
    app.run(host='0.0.0.0')
