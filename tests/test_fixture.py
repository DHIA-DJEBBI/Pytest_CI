import pytest 

@pytest.fixture
def sample_list():
    return [1,3,7]

def test_sum(sample_list):
    assert sum(sample_list)==11

@pytest.mark.xfail(reason="Bug 1332 ")
def test_len(sample_list): 
    assert len(sample_list)==4

@pytest.mark.skip(reason="Bug 2 ")
def test_len1(sample_list): 
    assert len(sample_list)==10


