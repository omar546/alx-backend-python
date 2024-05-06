#!/usr/bin/env python3
"""
Asyncio Tasks
"""
import asyncio
import random
from typing import List

file = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Takes: max delay (int, opt)
    Return: Asyncio Tasks
    """
    return asyncio.create_task(file(max_delay))
