import pytest 

# test_fixture_yield.py
import pytest

@pytest.fixture

def db_connection():
    print("\n[SETUP] Opening DB connection")
    conn = {"status": "connected"}
    yield conn
    print("\n[TEARDOWN] Closing DB connection")
    conn["status"] = "disconnected"
    # yield conn

def test_db_query(db_connection):
    assert db_connection["status"] == "connected" 







