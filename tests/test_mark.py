# test_marks.py
import pytest

@pytest.mark.skip(reason="Feature not ready")
def test_skip_example():
    assert 1 == 2

@pytest.mark.skipif(2 + 2 != 4, reason="Maths is broken")
def test_skipif_example():
    assert 2 + 2 == 4

@pytest.mark.xfail(reason="Bug not fixed yet")
def test_xfail_example():
    assert 10 / 0 == 0  # division by zero

@pytest.mark.api
def test_api():
    assert "py" in "pytest"

@pytest.mark.ui
def test_ui():
    assert len([1, 2, 3]) == 3
