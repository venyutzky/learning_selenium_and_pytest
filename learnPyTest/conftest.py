import pytest


@pytest.fixture(scope="session", autouse=True)
def tc_setup():
    print("Launch browser")
    print("Login")
    print("Browse Products")
    yield
    print("Logoff")
    print("Close browser")