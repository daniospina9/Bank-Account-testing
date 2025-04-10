def sum(a, b):
    """
    >>> sum(5, 7)
    12

    >>> sum(4, -4)
    0
    """
    return a + b

def subtract(a, b):
    """
    >>> subtract(5, 2)
    3

    >>> subtract(8, 12)
    -4
    """
    return a - b

def multiply(a, b):
    """
    >>> multiply(4, 5)
    20

    >>> multiply(80, 0)
    0

    >>> multiply(150, 1)
    150
    """
    return a * b

def divide(a, b):
    """
    >>> divide(10, 0)
    Traceback (most recent call last):
    ValueError: Division not permited
    """
    if b == 0:
        raise ValueError("Division not permited")
    return a / b