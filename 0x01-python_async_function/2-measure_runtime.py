#!/usr/bin/env python3
"""
This module defines a function to measure the runtime of the wait_n coroutine.
"""
import time
import asyncio
wait_n = __import__("1-concurrent_corutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the total execution time for wait_n(n, max_delay) and returns
    the average time per coroutine call (total_time / n).

    Args:
        n (int): Number of times to call wait_n.
        max_delay (int): Maximum delay for wait_n.

    Returns:
        float: Average execution time per call.
    """
    start_time = time.time()  # Record start time
    asyncio.run(wait_n(n, max_delay))  # Run wait_n
    end_time = time.time()  # Record end time

    total_time = end_time - start_time  # Calculate total execution time
    return total_time / n  # Return the average time
