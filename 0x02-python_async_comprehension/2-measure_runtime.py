#!/usr/bin/env python3
"""Returns total runtime in seconds for running 'async_comprehension' 4 times."""

import asyncio
import time

file = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Returns:
        Total runtime in seconds (float).
    """
    start_time = time.time()
    await asyncio.gather(*(file() for _ in range(4)))
    total_runtime = time.time() - start_time

    return total_runtime
