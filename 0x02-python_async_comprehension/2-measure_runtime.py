#!/usr/bin/env python3
"""ASYNC Comprehension Module."""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Spawn three async_comprehension and return its runtime."""
    started = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    elased = time.perf_counter() - started
    return elased
