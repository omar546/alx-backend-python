#!/usr/bin/env python3
"""
Tasks II
"""

import asyncio
import random
from typing import List


file = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Executes task_wait_random for n times."""

    times = await asyncio.gather(
        *tuple(map(lambda _: file(max_delay), range(n)))
    )
    return sorted(times)
