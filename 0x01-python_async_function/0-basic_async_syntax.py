#!/usr/bin/env python3
"""
The basics of async
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Takes: max_delay int (Defaults to 10)
    Returns: a random float after random time
    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
