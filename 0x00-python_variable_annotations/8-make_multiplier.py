#!/usr/bin/env python3
"""ALX SE Backend Module."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a callable,"""
    def fn(mult: float) -> float:
        """Return the product of the number"""
        return mult * multiplier
    return fn
