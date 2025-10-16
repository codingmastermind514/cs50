# importing
from fuel import convert
from fuel import gauge
import pytest

# testing convert function
def test_convert():

    # test valid
    assert convert("1/4") == 25
    assert convert("1/10") == 10
    assert convert("1/5") == 20

    # test for smaller denominator
    with pytest.raises(ValueError):
        convert("100/1")

    # test for invalid input
    with pytest.raises(ValueError):
        convert("cat/horse")
    with pytest.raises(ZeroDivisionError):
        convert("100/0")
    with pytest.raises(ValueError):
        convert("-1/7")
    with pytest.raises(ValueError):
        convert("1/-7")

# test gauge function
def test_gauge():
    assert gauge(87) == "87%" # normal percentage
    assert gauge(1) == "E" # empty
    assert gauge(99) == "F" # full
    assert gauge(50) == "50%" # normal percentage


