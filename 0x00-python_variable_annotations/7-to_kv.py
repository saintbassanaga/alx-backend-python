#!/usr/bin/env python3
"""ALX SE Backend Module."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    "Return a tuple of string and float."
    return k, v**2
