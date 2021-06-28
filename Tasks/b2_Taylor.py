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
    f = 1
    for i in range(0, 100):
        f *= i
        if f == 0:
            f = 1
        e = e + (x ** i) / f
    return e


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    e = 0
    q = x
    for i in range(0, 50):
        if i != 0:
            q = q * (-1) * (x * x) / ((2 * i + 1) * (2 * i))
        e += q
    return e


if __name__ == '__main__':
    print(sinx(1.55433))
    print(math.sin(1.55433))
    print(ex(1.55433))
    print(math.exp(1.55433))
