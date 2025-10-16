from seasons import convert
import pytest
from datetime import date

# tests invalid input
def test_invalid():
    with pytest.raises(SystemExit):
        convert("fgfg-ff-sk") # non date
    with pytest.raises(SystemExit):
        convert("10-20-2021") # no 20th month
    with pytest.raises(SystemExit):
        convert("6767-4-4") # no 6767th day
    with pytest.raises(SystemExit):
        convert("2020-20-20") # wrong format
    with pytest.raises(SystemExit):
        convert("2020-10-8888888") # wrong dae and in far future
    with pytest.raises(SystemExit):
        convert("2020") # missing month and day
