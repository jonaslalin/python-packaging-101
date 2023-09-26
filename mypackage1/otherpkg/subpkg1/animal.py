import json
from typing import List, cast

from importlib_resources import files

import otherpkg.subpkg1.resources1 as resources1


def is_animal(guess: str) -> bool:
    with files(resources1).joinpath("animals.json").open() as f:
        animals = cast(List[str], json.load(f))
    return guess in animals


def is_animal2(guess: str) -> bool:
    text = files(resources1).joinpath("animals.json").read_text()
    animals = cast(List[str], json.loads(text))
    return guess in animals
