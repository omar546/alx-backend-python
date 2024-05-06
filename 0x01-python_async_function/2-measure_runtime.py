#!/usr/bin/env python3
"""
Measure the runtime
"""
import asyncio
import random
import time

file = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Takes: n (int), max_delay (int, opt)
    Returns: float(time)
    """
    start = time.perf_counter()
    asyncio.run(file(n, max_delay))
    end = time.perf_counter()
    return (end - start) / n
