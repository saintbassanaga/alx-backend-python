#!/usr/bin/env python3
"""ALX SE Backend Module."""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    "Return the sum of list of float and int."
    return sum(mxd_lst)
