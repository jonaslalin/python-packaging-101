from typing import List
from fibo import fib2


def fib2_inclusive(n: int) -> List[int]:
    result = fib2(n)
    a, b = result[-2], result[-1]
    a, b = b, a + b
    if b == n:
        result.append(b)
    return result
