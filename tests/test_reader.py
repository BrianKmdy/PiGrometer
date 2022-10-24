import pytest
import sys
import time
import random


@pytest.fixture
def _reader(mocker):
    mocker.patch('pigrometer.DB_PATH', '/tmp/pigrometer.db')

    sys.modules['sqlite3'] = mocker.MagicMock()
    sys.modules['adafruit_dht'] = mocker.MagicMock()
    sys.modules['board'] = mocker.MagicMock()

    from pigrometer import reader

    _reader = reader.Reader(
        reader.Reader.DEFAULT_PERIOD,
        reader.Reader.DEFAULT_DHT_VERSION,
        reader.Reader.DEFAULT_DHT_PIN)

    mocker.patch.object(_reader, '_get_time_to_next_period',
                        mocker.MagicMock(return_value=0.01))

    yield _reader


def test_reader(mocker, _reader):
    mock_dht_device = mocker.MagicMock()
    mock_temperature = mocker.PropertyMock(
        side_effect=lambda: random.uniform(-1000, 1000))
    mock_humidity = mocker.PropertyMock(
        side_effect=lambda: random.uniform(-1000, 1000))
    type(mock_dht_device).temperature = mock_temperature
    type(mock_dht_device).humidity = mock_humidity
    mocker.patch.object(_reader, '_get_dht_device',
                        mocker.MagicMock(return_value=mock_dht_device))

    mock_db_connection, mock_db_cursor = mocker.MagicMock(), mocker.MagicMock()
    mocker.patch.object(_reader, '_open_db_connection', mocker.MagicMock(
        return_value=(mock_db_connection, mock_db_cursor)))

    _reader.start()
    time.sleep(1)
    assert (_reader.is_alive() == True)
    _reader.terminate.set()
    _reader.join(1)
    assert (_reader.is_alive() == False)

    assert (len(mock_db_cursor.mock_calls) > 0)
    assert (mock_temperature.called)
    assert (mock_humidity.called)
    assert (len(mock_db_cursor.mock_calls) - 1 == mock_temperature.call_count
            and len(mock_db_cursor.mock_calls) - 1 == mock_humidity.call_count)


def test_reader_exception(mocker, _reader):
    mock_dht_device = mocker.MagicMock()
    mock_temperature = mocker.PropertyMock(
        return_value=13, side_effect=Exception)
    mock_humidity = mocker.PropertyMock(return_value=37)
    type(mock_dht_device).temperature = mock_temperature
    type(mock_dht_device).humidity = mock_humidity
    mocker.patch.object(_reader, '_get_dht_device',
                        mocker.MagicMock(return_value=mock_dht_device))

    _reader.start()
    time.sleep(1)
    assert (_reader.is_alive() == False)
    _reader.terminate.set()
    _reader.join()
