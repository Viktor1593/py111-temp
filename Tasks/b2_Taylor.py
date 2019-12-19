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

    print(x)
    if x == 0:
        return 1
    res_s = 0
    n = 1
    res = (x ** n) / math.factorial(n)
    while res > delta:
        res_s += res
        res = (x ** n) / math.factorial(n)
        n += 1

    return res_s


def sinx(x: Union[int, float]) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """


    print(x)
    return 0


if __name__ == '__main__':
	print(ex(1))