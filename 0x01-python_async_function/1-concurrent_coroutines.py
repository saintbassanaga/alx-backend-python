#!/usr/bin/env python3
"""ASYNC IO Module."""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Run wait_random n times and return a list of it output."""
    out = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(out)
