import pytest

@pytest.mark.sanity
def testLogin():
    print("Login Successful")

@pytest.mark.regression
def testCalculation():
    assert 2+2 == 4

def testLogoff():
    print("Logout Successful")