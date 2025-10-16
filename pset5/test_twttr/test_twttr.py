# import
from twttr import shorten

# test lowercase
def test_lower():
    assert shorten("twitter") == "twttr"
    assert shorten("cat") == "ct"
    assert shorten("you") == "y"

# test upper case
def test_upper():
    assert shorten("TWITTER") == "TWTTR"
    assert shorten("CAT") == "CT"
    assert shorten("YOU") == "Y"

# test mixed case
def test_mixed():
    assert shorten("TwItTeR") == "TwtTR"
    assert shorten("Cat") == "Ct"
    assert shorten("cAT") == "cT"

# test nothing
def test_nowt():
    assert shorten(" ") == " "
    assert shorten("") == ""

# test weird symbols
def test_weird():
    assert shorten("hi1234567890") == "h1234567890" # removes vowels only ; ignores weird symbols
    assert shorten("aeiou") == "" #
    assert shorten("aeiouœ∑´®†¥¨ˆøπåß∂ƒ©˙∆˚¬…æ“‘«≈ç√∫˜µ≤≥÷¡™£¢∞§¶•ªº") == "œ∑´®†¥¨ˆøπåß∂ƒ©˙∆˚¬…æ“‘«≈ç√∫˜µ≤≥÷¡™£¢∞§¶•ªº"
    assert shorten("aeiou!(),.;'+=-_--?&~") == "!(),.;'+=-_--?&~"
