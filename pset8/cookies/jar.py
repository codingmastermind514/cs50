# jar class
class Jar:
    # init
    def __init__(self, capacity=12):
        self._capacity = capacity # capacity
        self._size = 0 # size
        # if cacity is non int: value error
        if type(capacity) != int:
            raise ValueError("sad meow")
        # if cacity is non positive: value error
        if capacity < 0:
            raise ValueError("sad meow")

   # return size num of cookies
    def __str__(self):
        return "🍪" * self._size

    def deposit(self, n):
        # if deposit is non int: value error
        if type(n) != int:
            raise ValueError("you big back u eat 2 much 🍪")

        # if capacity overflow: value error
        if self._size + n > self._capacity or n < 0:
            raise ValueError("you big back u eat 2 much 🍪")
        # if passes check add to cookie jar
        self._size += n


    def withdraw(self, n):
        # if withdrawal is non int value error
        if type(n) != int:
            raise ValueError("you big back u eat 2 much 🍪")

         # if withdrawal or size is non positive value error
        if n > self._size or n < 0:
            raise ValueError("you big back u eat 2 much 🍪")

        # if passes all checks then withdraw
        self._size -= n

    # capacity should return the cookie jar’s capacity.
    @property
    def capacity(self):
        return self._capacity

    # size should return the number of cookies actually in the cookie jar, initially 0.
    @property
    def size(self):
        return self._size
