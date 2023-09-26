import pytest

from fibo import fib, fib2


def test_fib(capsys: pytest.CaptureFixture[str]) -> None:
    fib(10)
    out, err = capsys.readouterr()
    assert out == "0 1 1 2 3 5 8 \n"


def test_fib2() -> None:
    assert fib2(7) == [0, 1, 1, 2, 3, 5]
    assert fib2(8) == [0, 1, 1, 2, 3, 5]
    assert fib2(9) == [0, 1, 1, 2, 3, 5, 8]
