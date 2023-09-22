from otherpkg.reduce import reduce


def test_sum() -> None:
    assert reduce(1, 2, 3, 4, 5, acc=0) == 15
    assert reduce("a", "b", "c", acc="") == "abc"
