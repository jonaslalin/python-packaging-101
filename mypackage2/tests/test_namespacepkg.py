import pytest

from namespacepkg.foo.bar.baz import fizz_buzz


@pytest.mark.parametrize(
    ("value", "expected"),
    [
        (1, "1"),
        (2, "2"),
        (3, "fizz"),
        (4, "4"),
        (5, "buzz"),
        (6, "fizz"),
        (7, "7"),
        (8, "8"),
        (9, "fizz"),
        (10, "buzz"),
        (11, "11"),
        (12, "fizz"),
        (13, "13"),
        (14, "14"),
        (15, "fizz buzz"),
        (16, "16"),
        (17, "17"),
        (18, "fizz"),
        (19, "19"),
        (20, "buzz"),
        (21, "fizz"),
        (22, "22"),
        (23, "23"),
        (24, "fizz"),
        (25, "buzz"),
        (26, "26"),
        (27, "fizz"),
        (28, "28"),
        (29, "29"),
        (30, "fizz buzz"),
        (31, "31"),
        (32, "32"),
        (33, "fizz"),
        (34, "34"),
        (35, "buzz"),
        (36, "fizz"),
    ],
)
def test_fizz_buzz(value: int, expected: str) -> None:
    assert fizz_buzz(value) == expected
