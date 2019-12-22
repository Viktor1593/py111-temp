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
    res_s = 1
    n = 1
    res = (-1)**n * (x ** n) / math.factorial(n)
    while abs(res) > delta:
        #res_s += (-1)**n * (x ** n) / math.factorial(n)
        res_s += res
        res = (-1)**n * (x ** n) / math.factorial(n)
        n += 1

    return res_s


def sinx(x: Union[int, float], delta = 0.0001) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    print(x)
    y = 0
    k = 0
    a=((-1)**k)*(x**(1+2*k))/math.factorial(1+2*k)
    while abs(a) > delta:
        y+=((-1)**k)*(x**(1+2*k))/math.factorial(1+2*k)
        #y = y + a
        a=((-1)**k)*(x**(1+2*k))/math.factorial(1+2*k)
        k += 1
        #print(a)
    return y

if __name__ == '__main__':
    const = 1.55433
    print(math.exp(const))
    print(ex(const))
    print(sinx(const))
    print(math.sin(const))