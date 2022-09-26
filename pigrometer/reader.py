import Adafruit_DHT
import sqlite3
import argparse
import traceback
import time
import datetime

# Default pin setup for the DHT22 sensort on the raspberry pi
DEFAULT_DHT_MODEL = 22
DEFAULT_DHT_PIN = 4
# Default period length (seconds) for readings
DEFAULT_PERIOD = 60

class HumidityReader():
    def __init__(self, period):
        self.period = int(period)
        self.current_start_of_period = 0
        if self.period < 1:
            raise Exception('Period must be greater than or equal to 1')
    
    def get_start_of_period(self):
        return int(time.time() / 60) * 60

    def run(self):
        self.current_start_of_period = self.get_start_of_period()
        while True:
            try:
                # Store the reading from the current period
                humidity, temperature = Adafruit_DHT.read_retry(DEFAULT_DHT_MODEL, DEFAULT_DHT_PIN)
                print('At {}: temp {:.1f}C humidity {:.1f}%'.format(datetime.datetime.fromtimestamp(self.current_start_of_period).strftime('%m-%d %H:%M:%S'), temperature, humidity))
                cur.execute('INSERT INTO humidity VALUES (?, ?, ?)', (self.current_start_of_period, humidity, temperature))
                con.commit()
            except sqlite3.IntegrityError:
                traceback.print_exc()

            # Sleep until the start of the next period
            self.current_start_of_period += self.period
            time.sleep(self.current_start_of_period - time.time())

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Raspberry pi temperature and humidity reader')
    parser.add_argument('-p', '--period', type=int, default=DEFAULT_PERIOD,
        help='The length of a period (seconds), this is the length of time between readings')
    args = parser.parse_args()

    # Connect to the db and create the table if it doesn't exist
    con = sqlite3.connect('humidity.db')
    cur = con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS humidity (epoch bigint NOT NULL UNIQUE, temperature real, humidity real)')

    try:
        # Start the humidity reader
        reader = HumidityReader(args.period)
        reader.run()
    except KeyboardInterrupt:
        pass

    con.close()

