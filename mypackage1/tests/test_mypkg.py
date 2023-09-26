from typing import List

import pytest

from mypkg.subpkg1.fibo import fib2_inclusive
from mypkg.subpkg1.hello import hello


def test_fib2_inclusive() -> None:
    assert fib2_inclusive(7) == [0, 1, 1, 2, 3, 5]
    assert fib2_inclusive(8) == [0, 1, 1, 2, 3, 5, 8]
    assert fib2_inclusive(9) == [0, 1, 1, 2, 3, 5, 8]


@pytest.mark.parametrize(
    ("n", "expected"),
    [
        (0, [0]),
        (1, [0, 1, 1]),
        (2, [0, 1, 1, 2]),
        (3, [0, 1, 1, 2, 3]),
        (4, [0, 1, 1, 2, 3]),
    ],
)
def test2_fib2_inclusive(n: int, expected: List[int]) -> None:
    assert fib2_inclusive(n) == expected


def test_hello() -> None:
    assert hello("World") == "Hello, World!"
