#!/usr/bin/env python3
"""Yield random float value between 0 and 10 after a 1-second delay in each iteration."""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Yields:
        random (float) between 0 and 10.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
