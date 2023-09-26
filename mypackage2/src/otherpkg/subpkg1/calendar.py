import json
from dataclasses import dataclass
from typing import List, cast

from importlib_resources import files
from typing_extensions import TypedDict


@dataclass
class Holiday:
    name: str
    date: str


Holidays = List[Holiday]


class SerializedHoliday(TypedDict):
    name: str
    date: str


SerializedHolidays = List[SerializedHoliday]


def holidays() -> Holidays:
    text = files("otherpkg.subpkg1").joinpath("holidays.json").read_text()
    serialized_holidays = cast(SerializedHolidays, json.loads(text))
    _holidays = [Holiday(**h) for h in serialized_holidays]
    return _holidays
