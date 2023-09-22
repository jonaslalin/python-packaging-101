from otherpkg.reduce import reduce
from otherpkg.subpkg1.sigmoid import goodbye_sigmoid


def test_reduce() -> None:
    assert reduce(1, 2, 3, 4, 5, acc=0) == 15
    assert reduce("a", "b", "c", acc="") == "abc"


def test_goodbye_sigmoid() -> None:
    assert goodbye_sigmoid(0) == "Goodbye, 0.5!"
