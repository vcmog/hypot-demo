def squared(a):
    """Square a number

    :param a: Number
    :type a: int, float
    :return: Squared number
    :rtype: int, float
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
    """Calculate hypotenuse from the lengths of the shorter 2 sides.

    :param a: First length.
    :type a:  int or float
    :param b: Second length.
    :type b: int or float
    :return: Length of the hypotenuse.
    :rtype: int or float.
    """
    sa = squared(a)
    sb = squared(b)
    sumAB = addition(sa, sb)

    return sqroot(sumAB)
