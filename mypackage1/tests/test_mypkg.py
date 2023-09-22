from mypkg.subpkg1.hello import hello
from mypkg.subpkg1.fibo import fib2_inclusive


def test_fib2_inclusive() -> None:
    assert fib2_inclusive(7) == [0, 1, 1, 2, 3, 5]
    assert fib2_inclusive(8) == [0, 1, 1, 2, 3, 5, 8]
    assert fib2_inclusive(9) == [0, 1, 1, 2, 3, 5, 8]


def test_hello() -> None:
    assert hello("World") == "Hello, World!"
