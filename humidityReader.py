import sqlite3
import Adafruit_DHT
import time
import traceback

DHT_MODEL = 22
DHT_PIN = 4

con = sqlite3.connect('humidity.db')
cur = con.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS humidity (epoch bigint NOT NULL UNIQUE, temperature real, humidity real)')

try:
    while True:
        epoch = int(time.time() / 60) * 60
        humidity, temperature = Adafruit_DHT.read_retry(DHT_MODEL, DHT_PIN)
        print('Time {}: temperature {:.1f} humidity {:.1f}'.format(epoch, temperature, humidity))
        cur.execute('INSERT INTO humidity VALUES (?, ?, ?)', (epoch, humidity, temperature))
        con.commit()
        time.sleep((int(time.time() / 60) + 1) * 60 - time.time())
except KeyboardInterrupt:
    pass
except Exception as e:
    traceback.print_exc(e)

con.close()