from numb3rs import validate

# valid IPv4 adresses
def test_valid():
    assert validate("255.255.255.255") == True
    assert validate("2.1.3.4") == True
    assert validate("144.50.99.45") == True
    assert validate("23.23.23.23") == True
    assert validate("21.12.21.21") == True
    assert validate("45.45.54.54") == True
    assert validate("87.200.230.65") == True

# invalid IPv4 adresses
def test_invalid():
    assert validate("512.512.512.512") == False
    assert validate("512.103..512") == False
    assert validate("123") == False
    assert validate("abc.def.fgh.ijk") == False
    assert validate("hhh.hhh.hhjh") == False
    assert validate(" ") == False
    assert validate("400.100.213.435") == False
    assert validate("foo bear") == False
    assert validate("125.103.101.512") == False
