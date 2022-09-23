def add(x, y):
    assert isinstance(x, (int, float)) and isinstance(y, (int, float)), "Only int or float can be added"
    assert x > 0 and y > 0, "numbers cannot be negative"
    return x + y

assert[1, 2, 3] == [1, 2, 3]
print(add(-2, 3))

import doctest

def add(x, y):
    """ adds two numbers
    >>> add(5, 5)
    11
    >>> add( 2, -6)
    -4
    """
    return x + y
if __name__ == "__main__":
    doctest.testmod()