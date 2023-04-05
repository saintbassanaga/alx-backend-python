#!/usr/bin/env python3
"""ASYNC IO Module."""
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Run task_wait_random n times and return a list of it output."""
    out = await asyncio.gather(
            *(task_wait_random(max_delay) for _ in range(n)))
    return sorted(out)
