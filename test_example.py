import pytest

import jaybird_420 as jb

def test_sqrt_is_positive():
    test_value = 10
    assert jb.sqrt(test_value) > 0

def test_sqrt_is_zero():
    test_value = 0
    assert jb.sqrt(test_value) == 0

def test_sqrt_negative_gives_error():
    test_value = -1
    with pytest.raises(ValueError):
        jb.sqrt(test_value)

