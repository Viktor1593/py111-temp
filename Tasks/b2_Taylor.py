"""
Taylor series
"""
from typing import Union
import math


def ex(x: Union[int, float], delta = 0.0001) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    if x == 0:
        return 1
    s = 0
    i = 0
    while True:
        a = x**i/math.factorial(i)
        i += 1
        s+=a
        if abs(a) < delta:
            break

    return s


def sinx(x: Union[int, float], delta = 0.0001) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    a = x
    s = a
    i = 1
    while abs(a) > delta:
        a *= -1 * x**2 / ((2 * i) * (2 * i + 1))
        s += a
        i+=1
    return s

if __name__ == '__main__':
    const = 1.55433
    print(math.exp(const))
    print(ex(const))
    print(sinx(const))
    print(math.sin(const))