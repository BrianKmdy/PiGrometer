import pytest
import sqlite3
import os
import time
import json

TEST_DB_PATH = '/tmp/pigrometer.db'


@pytest.fixture(autouse=True)
def _server(mocker):
    mocker.patch('pigrometer.DB_PATH', TEST_DB_PATH)
    from pigrometer import server
    yield server


@pytest.fixture
def _database(mocker):
    if os.path.exists(TEST_DB_PATH):
        os.remove(TEST_DB_PATH)

    db_connection = sqlite3.connect(TEST_DB_PATH)
    db_cursor = db_connection.cursor()
    db_cursor.execute(
        'CREATE TABLE IF NOT EXISTS humidity (epoch bigint NOT NULL UNIQUE, temperature real, humidity real)')

    yield db_connection, db_cursor
    db_connection.close()
    os.remove(TEST_DB_PATH)


def test_route_home(_server):
    response = _server.app.test_client().get('/')
    assert (response.status_code == 200)


@pytest.mark.parametrize('history, granularity',
                         [
                             (1, 60),
                             (3, 900),
                             (14, 18000),
                         ])
def test_route_data_simple(mocker, _server, _database, history, granularity):

    response = _server.app.test_client().get(
        '/data', query_string=f'history={history}&granularity={granularity}')
    assert (response.status_code == 200)
    assert (len(response.json) == 0)


@pytest.mark.skip(reason="Need to update API to take start and end time,\
                          this breaks right now because the server relies on time.time()")
@pytest.mark.parametrize('time_offsets, temperatures, humidities, history, granularity',
                         [
                             ([2700, 1800, 900], [0, 1, 2], [0, 1, 2], 1, 900),
                             ([240, 180, 120, 60, 0], [0, 1, 2, 55, 3],
                              [0, 2, 6, 8, -2], 1, 60),
                             ([4, 3, 2], [0, 1, 21], [0, 51, 2], 1, 1)
                         ])
def test_route_data_advanced(mocker, _server, _database, time_offsets, temperatures, humidities, history, granularity):
    epochs = [int(time.time() / granularity) *
              granularity - t for t in time_offsets]

    db_connection, db_cursor = _database
    for epoch, temperature, humidity in zip(epochs, temperatures, humidities):
        db_cursor.execute('INSERT INTO humidity VALUES (?, ?, ?)',
                          (epoch, humidity, temperature))
        db_connection.commit()

    response = _server.app.test_client().get(
        '/data', query_string=f'history={history}&granularity={granularity}')
    assert (response.status_code == 200)
    assert (len(json.loads(response.json)) == len(epochs))

    for response_data, epoch, temperature, humidity in zip(json.loads(response.json), epochs, temperatures, humidities):
        r_epoch, r_humidity, r_temperature = response_data
        assert (r_epoch == epoch)
        assert (r_temperature == temperature)
        assert (r_humidity == humidity)
