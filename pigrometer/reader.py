import board
import adafruit_dht
import sqlite3
import time
import datetime
import os
import threading

from pigrometer import DB_PATH

class Reader(threading.Thread):
    DEFAULT_PERIOD = 60

    # Default pin setup for the DHT22 sensort on the raspberry pi
    DEFAULT_DHT_VERSION = 'DHT22'
    DEFAULT_DHT_PIN = 'D4'
    DHT_READ_RETRIES = 3

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
        return int(time.time() / self.period) * self.period

    def _get_time_to_next_period(self):
        return (self.current_start_of_period + self.period) - time.time()

    def _get_dht_device(self):
        return getattr(adafruit_dht, self.dht_version)(getattr(board, self.dht_pin))

    def _get_dht_reading(self, dht_device):
        for i in range(0, Reader.DHT_READ_RETRIES):
            try:
                return dht_device.temperature, dht_device.humidity
            except RuntimeError:
                time.sleep(1)
        raise RuntimeError

    def _open_db_connection(self):
        # Connect to the db and create the table if it doesn't exist
        db_connection = sqlite3.connect(DB_PATH)
        db_cursor = db_connection.cursor()
        return db_connection, db_cursor

    def run(self):
        if not os.path.exists(os.path.dirname(DB_PATH)):
            os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

        db_connection, db_cursor = self._open_db_connection()
        db_cursor.execute('CREATE TABLE IF NOT EXISTS humidity (epoch bigint NOT NULL UNIQUE, temperature real, humidity real)')

        dht_device = self._get_dht_device()

        self.current_start_of_period = self._get_start_of_period()
        while not self.terminate.is_set():
            try:
                # Store the reading from the current period
                temperature, humidity = self._get_dht_reading(dht_device)
                if temperature is None or humidity is None:
                    raise RuntimeError()

                print('At {}: temp {:.1f}C humidity {:.1f}%'.format(datetime.datetime.fromtimestamp(self.current_start_of_period).strftime('%m-%d %H:%M:%S'), temperature, humidity))
                db_cursor.execute('INSERT INTO humidity VALUES (?, ?, ?)', (self.current_start_of_period, humidity, temperature))
                db_connection.commit()
            except RuntimeError:
                print('Unable to get a reading from the DHT sensor')
            except sqlite3.IntegrityError:
                pass

            # Sleep until the start of the next period
            self.terminate.wait(self._get_time_to_next_period())
            self.current_start_of_period += self.period

        db_connection.close()