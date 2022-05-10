import flask
import sqlite3
import datetime

app = flask.Flask(__name__)

@app.route('/')
def hello_world():
    con = sqlite3.connect('humidity.db')
    response = '<br>'.join(['{}: {:.1f}C {:.1f}%'.format(datetime.datetime.fromtimestamp(epoch), t, h) for epoch, h, t in con.cursor().execute('SELECT * from humidity')])
    con.close()
    return response

if __name__ == '__main__':
    app.run(host='0.0.0.0')