from math import exp
from typing import Union


def sigmoid(x: Union[float, int]) -> float:
    return 1 / (1 + exp(-x))
