#!/usr/bin/env python3
"""ALX SE Backend Module."""
from typing import Sequence, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Return an element from the sequence or none."""
    if lst:
        return lst[0]
    else:
        return None
