# import
from bank import value

# test uppercase
def test_upper():
    assert value("HELLO NEWMAN") == 0
    assert value("HEY") == 20
    assert value("SUP") == 100

# test lowercase
def test_lower():
    assert value("hello newman") == 0
    assert value("hey") == 20
    assert value("sup") == 100

# test mixed  case
def test_mixed():
    assert value("newman HELLO") == 100
    assert value("hEY") == 20
    assert value("Sup") == 100

# test for no greeting
def test_nowt():
    assert value("") == 100
    assert value(" ") == 100

# test random symbols
def test_weird():
    assert value("newman HELLO¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æ≈ç√∫˜µ≤≥÷") == 100 # random keystrokes not starting w/ 'h' = $100
    assert value("newman HELLO!(),.;'+=-_--?&~") == 100
    assert value("hEY¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æ≈ç√∫˜µ≤≥") == 20
    assert value("hEY!(),.;'+=-_--?&~") == 20
    assert value("Sup¡™£¢∞§¶•ªº–≠œ∑´®†¥¨ˆøπ“‘«åß∂ƒ©˙∆˚¬…æ≈ç√∫˜µ≤≥÷") == 100
    assert value("Sup!(),.;'+=-_--?&~") == 100
