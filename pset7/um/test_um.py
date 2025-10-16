from um import count

# strings with no ums or strings with ums only inside words
def test_none():
    assert count("i am a gummy yummy foo bear") == 0
    assert count("you ummy bum") == 0
    assert count("ummybummyinmytummy") == 0
    assert count("yUM bum") == 0

# strings that have ums
def test_um():
    assert count("he ended with 'um' and a long pause") == 1
    assert count("he muttered um, um, um under his breath") == 3
    assert count("super-um-powered robots are funny and um strange") == 2
    assert count("hum… um—mum didn't notice") == 1

# case-insensitivity
def test_UM():
    assert count("Um, you really think so") == 1
    assert count("he replied UM? like she didn't understand") == 1
    assert count("UM UM UM UM everywhere in the speech") == 4

