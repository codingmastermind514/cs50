from jar import Jar
import pytest

# test init function
def test_init():
    # valid
    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0

    # invalid
    with pytest.raises(ValueError):
        jaaaaar = Jar(6.999) # non int
    with pytest.raises(ValueError):
        jaaaaar = Jar(-6999) # negative int
    with pytest.raises(ValueError):
        jaaaaar = Jar("sad vroom vroom") # non int
# test str
def test_str():
    jar = Jar()
    assert str(jar) == "" # no cookies
    jar.deposit(1)
    assert str(jar) == "🍪" # one cookie
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪" # 11 cookies

# test deposit
def test_deposit():
    jar = Jar()
    jar.deposit(4)
    assert jar.size == 4  # valid
    # test over capacity
    with pytest.raises(ValueError):
        jar.deposit(67676767676767)
    # test neg
    with pytest.raises(ValueError):
        jar.deposit(-67676767676767)
    # test non-int
    with pytest.raises(ValueError):
        jar.deposit(7.67)

def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(4)
    assert jar.size == 6  # valid
    with pytest.raises(ValueError):
        jar.withdraw(7.67) # test non-int
    with pytest.raises(ValueError):
        jar.withdraw(-7) # test neg
    with pytest.raises(ValueError):
        jar.withdraw(88888888)  # test over capacity
