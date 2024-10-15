#!/usr/bin/env python3
"""
This module defines a coroutine that measures the runtime of executing
async_comprehension four times in parallel and returns the total runtime.
"""

import time
import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the runtime of executing async_comprehension
    four times concurrently.

    The function uses asyncio.gather to run async_comprehension
    four times in parallel.
    It returns the total runtime as a float in seconds.

    Returns:
        float: The total runtime of the asynchronous operations.
    """
    start_time = time.time()  # Record the start time

    # Run async_comprehension four times concurrently
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()  # Record the end time

    # Calculate the total runtime
    total_runtime = end_time - start_time
    return total_runtime
