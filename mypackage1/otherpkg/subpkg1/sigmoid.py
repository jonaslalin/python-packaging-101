from math import exp
from typing import Union
from mypkg.subpkg2.goodbye import goodbye


def sigmoid(x: Union[float, int]) -> float:
    return 1 / (1 + exp(-x))


def goodbye_sigmoid(x: Union[float, int]) -> str:
    return goodbye(str(sigmoid(x)))
