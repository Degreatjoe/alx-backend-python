#!/usr/bin/env python3
"""
This module defines an asynchronous coroutine that spawns multiple
wait_random coroutines and returns a list of delays in ascending order.
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay.
    Collects and returns a list of delays in ascending order.

    Args:
        n (int): Number of times to spawn wait_random.
        max_delay (int): Maximum delay for wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    delays = []
    for _ in range(n):
        delays.append(await wait_random(max_delay))

    # Create an empty result list
    sorted_delays = []

    # Sort the delays manually by iteratively finding the minimum
    while delays:
        min_delay = min(delays)
        delays.remove(min_delay)
        sorted_delays.append(min_delay)

    return sorted_delays
