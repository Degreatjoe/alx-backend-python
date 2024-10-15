#!/usr/bin/env python3
"""
This module defines a coroutine that measures the runtime of executing
async_comprehension four times in parallel.
"""
import time
import asyncio
async_comprehension = __import__("async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
    Executes async_comprehension four times in parallel and measures
    the total runtime.

    Returns:
        float: The total runtime in seconds.
    """
    start_time = time.time()  # Record start time

    # Execute async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))

    end_time = time.time()  # Record end time

    total_runtime = end_time - start_time  # Calculate total runtime
    return total_runtime
