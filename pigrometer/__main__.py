import argparse
from pigrometer.reader import Reader

DEFAULT_PERIOD = 60

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Raspberry pi temperature and humidity reader')
    parser.add_argument('-p', '--period', type=int, default=DEFAULT_PERIOD,
        help='The length of a period (seconds), this is the length of time between readings')
    args = parser.parse_args()

    reader = Reader(args.period)
    reader.run()