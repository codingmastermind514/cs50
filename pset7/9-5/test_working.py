from working import convert
import pytest

def test_valid():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    # assert convert("09:10 AM to 5 PM") == "09:10 to 17:00"
    assert convert("9:23 AM to 5:45 PM") == "09:23 to 17:45"
    assert convert("12:00 PM to 5:59 PM") == "12:00 to 17:59"
    assert convert("12:32 PM to 12:33 PM") == "12:32 to 12:33"
    assert convert("12:32 PM to 12:33 AM") == "12:32 to 00:33"

def test_invalid():
    # non-time
    with pytest.raises(ValueError):
        convert("gyhuuyghjgyhujjgh")
    with pytest.raises(ValueError):
        convert("9AMTO5PM")

    # lower AM/PM + spaces / format
    with pytest.raises(ValueError):
        convert("7 am to 9 am")
    with pytest.raises(ValueError):
        convert("5pm to 5:59 pm")
    with pytest.raises(ValueError):
        convert("5:1pm to 5:59 pm")

    # invalid / fake time
    with pytest.raises(ValueError):
        convert("67:00 AM to 4:00 PM")
    with pytest.raises(ValueError):
        convert("7:00 AM to 90:76 PM")
