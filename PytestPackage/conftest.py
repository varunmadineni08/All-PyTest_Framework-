import pytest

@pytest.fixture(autouse=True,scope="function")
def setup():
    print("[SETUP] Starting the test")
    yield
    print("[TEARDOWN] Closing the test after completed")

# we can use this conftest.py file for many files which is having fixtures need