#!/usr/bin/env python3
"""ALX SE Backend Module."""
from typing import Mapping, Union, Any, TypeVar

T = TypeVar('T')


def safely_get_value(
        dct: Mapping, key: Any,
        default: Union[T, None] = None) -> Union[Any, T]:
    """Return the value of the dict key of None."""
    if key in dct:
        return dct[key]
    else:
        return default
