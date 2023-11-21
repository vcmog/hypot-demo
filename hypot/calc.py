def squared(a):
    """
    Calculate the square of a number.

    Parameters:
    - a (int or float): The number to be squared.

    Returns:
    int or float: The square of the input number.
    """
    return a * a


def addition(a, b):
    """
    Add two numbers.

    Parameters:
    - a (int or float): The first number.
    - b (int or float): The second number.

    Returns:
    int or float: The sum of the two input numbers.
    """
    if isinstance(a, str) or isinstance(a, str):
        return "Please use integer or float"

    return a + b


def sqroot(a):
    """
    Calculate the square root of a number.

    Parameters:
    - a (int or float): The number for which the square root is calculated.

    Returns:
    float: The square root of the input number.
    """
    return a**0.5


def hypot(a, b):
    """
    Calculate the hypotenuse from the two shorter sides.

    Parameters:
    - a (int or float): The first length.
    - b (int or float): The second length.


    Returns:
    float: The length of the hypotenuse.
    """
    sa = squared(a)
    sb = squared(b)
    sumAB = addition(sa, sb)

    return sqroot(sumAB)
