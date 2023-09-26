from typing import List

from fibo import fib2


def fib2_inclusive(n: int) -> List[int]:
    if n == 0:
        return [0]
    elif n == 1:
        return [0, 1, 1]
    result = fib2(n)
    a, b = result[-2:]
    if (c := a + b) == n:
        result.append(c)
    return result
