from pigrometer.reader import Reader
from pigrometer.server import *
import argparse
import threading
import time

def run():
    reader = Reader(args.period, args.dht_version, args.dht_pin)
    reader.start()
    run_server()
    reader.terminate.set()
    reader.join()

def run_reader_only():
    reader = Reader(args.period, args.dht_version, args.dht_pin)
    reader.start()
    try:
        reader.join()
    except KeyboardInterrupt:
        reader.terminate.set()
        reader.join()

def run_server_only():
    run_server()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Raspberry pi temperature and humidity reader')
    parser.add_argument('-p', '--period', type=int, default=Reader.DEFAULT_PERIOD,
        help='The length of a period (seconds), this is the length of time between readings')
    parser.add_argument('--reader-only', action='store_true',
        help='Only run the temperature/humidity reader')
    parser.add_argument('--server-only', action='store_true',
        help='Only run the server')
    parser.add_argument('--dht-version', type=str, default=Reader.DEFAULT_DHT_VERSION,
        help='The version of the DHT sensor (either DHT 11 or DHT 22)')
    parser.add_argument('--dht-pin', type=str, default=Reader.DEFAULT_DHT_PIN,
        help='The GPIO on the raspberry pi that the DHT sensor is connected to')
    args = parser.parse_args()

    if args.reader_only:
        run_reader_only()
    elif args.server_only:
        run_server_only()
    else:
        run()