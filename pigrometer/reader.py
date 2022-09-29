import board
import adafruit_dht
import sqlite3
import time
import datetime
import os
import threading
import traceback

class Reader(threading.Thread):
    DATABASE = os.path.join(os.path.expanduser("~"), '.pigrometer', 'pigrometer.db')
    DEFAULT_PERIOD = 60

    # Default pin setup for the DHT22 sensort on the raspberry pi
    DEFAULT_DHT_VERSION = 'DHT22'
    DEFAULT_DHT_PIN = 'D4'
    DHT_READ_RETRIES = 10

    def __init__(self, period, dht_version, dht_pin):
        super().__init__()
        self.terminate = threading.Event()
        self.period = int(period)
        self.current_start_of_period = 0
        if self.period < 1:
            raise Exception('Period must be greater than or equal to 1')
        self.dht_version = dht_version
        self.dht_pin = dht_pin
    
    def _get_start_of_period(self):
        return int(time.time() / 60) * 60

    def _get_dht_reading(self, dhtDevice):
        for i in range(0, Reader.DHT_READ_RETRIES):
            try:
                return dhtDevice.temperature, dhtDevice.humidity
            except RuntimeError:
                traceback.print_exc()
                time.sleep(0.1)
        raise RuntimeError

    def run(self):
        # Connect to the db and create the table if it doesn't exist
        con = sqlite3.connect(Reader.DATABASE)
        cur = con.cursor()
        cur.execute('CREATE TABLE IF NOT EXISTS humidity (epoch bigint NOT NULL UNIQUE, temperature real, humidity real)')

        dhtDevice = getattr(adafruit_dht, self.dht_version)(getattr(board, self.dht_pin))

        self.current_start_of_period = self._get_start_of_period()
        while not self.terminate.is_set():
            try:
                # Store the reading from the current period
                temperature, humidity = self._get_dht_reading(dhtDevice)
                print('At {}: temp {:.1f}C humidity {:.1f}%'.format(datetime.datetime.fromtimestamp(self.current_start_of_period).strftime('%m-%d %H:%M:%S'), temperature, humidity))
                cur.execute('INSERT INTO humidity VALUES (?, ?, ?)', (self.current_start_of_period, humidity, temperature))
                con.commit()
            except RuntimeError:
                print('Unable to get a reading from the DHT sensor')
            except sqlite3.IntegrityError:
                pass

            # Sleep until the start of the next period
            self.current_start_of_period += self.period
            self.terminate.wait(self.current_start_of_period - time.time())

        con.close()