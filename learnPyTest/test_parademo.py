import pytest


# @pytest.fixture(params=['a', 'b'])
# def demo_fixture(request):
#     print(request.param)

@pytest.mark.parametrize("a, b, final", [(3,4,7), (1,3,4), (5,3,8)])
def testAdd(a,b,final):
    assert a+b==final

# def testLogin(demo_fixture):
#     print("Login Succesful")

# def testLogoff():
#     print("Logoff Succeful")

# def testCalculation():
#     assert 4 +2 == 6