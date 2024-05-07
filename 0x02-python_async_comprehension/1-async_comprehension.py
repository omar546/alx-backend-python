#!/usr/bin/env python3
"""Collects float values from 'async_generator' into a list."""

import asyncio
from typing import List

file = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronously collects float values from 'async_generator'.

    Returns:
        List[float]: Float values collected from 'async_generator'.
    """
    result = [i async for i in file()]
    return result
