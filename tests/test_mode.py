# test_modes.py
import pytest

def initialize(mode):
    if mode not in ["normal", "safe"]:
        raise ValueError("Mode invalide")
    return True

@pytest.mark.parametrize("mode", ["normal", "safe"])
def test_initialize_valid(mode):
    assert initialize(mode)

def test_initialize_invalid():
    with pytest.raises(ValueError, match="invalide"):
        initialize("debug")




