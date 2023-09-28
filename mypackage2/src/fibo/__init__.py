from typing import List


# write Fibonacci series up to n
def fib(n: int) -> None:
    a, b = 0, 1
    while a < n:
        print(a, end=" ")
        a, b = b, a + b
    print()


# return Fibonacci series up to n
def fib2(n: int) -> List[int]:
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a + b
    return result
