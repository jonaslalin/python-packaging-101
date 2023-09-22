from typing_extensions import Protocol, Self


class SupportsAdd(Protocol):
    def __add__(self, other: Self) -> Self:
        ...


def reduce(*args: SupportsAdd, acc: SupportsAdd) -> SupportsAdd:
    result = acc
    for value in args:
        result += value
    return result
