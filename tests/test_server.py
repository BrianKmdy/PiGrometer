from pyparsing import trace_parse_action
from pigrometer import server
import pytest
import requests

# TODO/bmoody Add the rest  of the assertions for these tests

# @pytest.fixture(scope="session")
# def app():
#     client = server.app.test_client()
# 
def test_index_route():
    response = server.app.test_client().get('/')

    assert(response.status_code == 200)
    # print(response)
    # print(response.data.decode('utf-8'))
    # assert response.status_code == 200
    # assert response.data.decode('utf-8') == 'Testing, Flask!'
# def test_server(_app):
#     print(requests.get('http://localhost:3000'))