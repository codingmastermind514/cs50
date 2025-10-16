from plates import is_valid

# vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters
def test_length():
    assert is_valid("SFR1111111111") == False
    assert is_valid("AA") == True

# all vanity plates must start with at least two letters
def test_start():
    assert is_valid("4AB") == False
    assert is_valid("A2BCD") == False
    assert is_valid("A2") == False
    assert is_valid("2A") == False
    assert is_valid("22") == False
    assert is_valid("CS50") == True
    assert is_valid("JH12") == True

# no periods, spaces, or punctuation marks are allowed
def test_weird():
    assert is_valid("CS@!AD") == False
    assert is_valid("SC¢∞") == False

# the first number used cannot be a ‘0’.
def test_zero():
    assert is_valid("AW09") == False
    assert is_valid("CB02") == False
    assert is_valid("AB3RD") == False

# numbers cannot be used in the middle of a plate; they must come at the end
def test_nums():
    assert is_valid("DS13H") == False
    assert is_valid("AA3RD") == False
    assert is_valid("44TH") == False

