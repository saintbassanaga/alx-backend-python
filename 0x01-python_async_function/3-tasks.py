#!/usr/bin/env python3
"""ASYNC IO Module."""
from asyncio import Task, create_task
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """Create and return a task using wait_random."""
    return create_task(wait_random(max_delay))
