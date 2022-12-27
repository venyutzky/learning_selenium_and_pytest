import pytest


@pytest.mark.skip
def testLogin():
    print("Login Successful")

@pytest.mark.regression
def testCalculation():
    assert 2+2 == 4

@pytest.mark.sanity
def testLogoff():
    print("Logout Successful")

@pytest.mark.xfail
def testCalculation1():
    assert 2+2 == 5