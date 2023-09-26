from otherpkg.reduce import reduce
from otherpkg.subpkg1.animal import is_animal, is_animal2
from otherpkg.subpkg1.calendar import holidays
from otherpkg.subpkg1.sigmoid import goodbye_sigmoid
from otherpkg.subpkg1.subsubpkg1.python import python_version


def test_reduce() -> None:
    assert reduce(1, 2, 3, 4, 5, acc=0) == 15
    assert reduce("a", "b", "c", acc="") == "abc"


def test_is_animal() -> None:
    assert is_animal("cat")
    assert not is_animal("car")


def test_is_animal2() -> None:
    assert is_animal2("cat")
    assert not is_animal2("car")


def test_holidays() -> None:
    assert "24th of December" in [h.date for h in holidays()]


def test_goodbye_sigmoid() -> None:
    assert goodbye_sigmoid(0) == "Goodbye, 0.5!"


def test_python_version() -> None:
    assert "Python version" in python_version()
