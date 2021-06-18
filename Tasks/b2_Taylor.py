"""
Taylor series
"""
from typing import Union
import math


def ex(x: Union[int, float]) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    e = 0
    for i in range(0, 100):
        e = e + (x ** i) / math.factorial(i)
    return e


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    e = 0
    for i in range(0, 50):
        e = e + (((-1) ** i) * (x ** (1 + 2 * i))) / math.factorial(1 + 2 * i)
    return e


if __name__ == '__main__':
    print(sinx(1.55433))
    print(math.sin(1.55433))
    print(ex(6))
