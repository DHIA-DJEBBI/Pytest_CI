import pytest 

def devide(a,b):
    return (a/b)

def pytest_configure(config):
    print("\n [HOOK] pytest is starting... ")


def test_devision_by_zero():
    with pytest.raises(ZeroDivisionError):
        devide(12,0)


