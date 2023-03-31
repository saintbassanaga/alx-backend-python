#!/usr/bin/env python3
"""ALX SE Backend Module."""
from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """Return a list."""
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in
