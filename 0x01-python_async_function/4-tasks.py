#!/usr/bin/env python3
"""
This module defines a function that spawns multiple tasks using
ask_wait_random
and returns a list of delays in ascending order.
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay.
    Collects and returns a list of delays in ascending order.

    Args:
        n (int): Number of times to call task_wait_random.
        max_delay (int): Maximum delay for task_wait_random.

    Returns:
        List[float]: List of delays in ascending order.
    """
    tasks = [task_wait_random(max_delay) for _ in range(n)]  # Create tasks
    delays = await asyncio.gather(*tasks)  # Gather results from tasks

    # Manually sort the delays by iteratively finding the minimum
    sorted_delays = []
    while delays:
        min_delay = min(delays)
        delays.remove(min_delay)
        sorted_delays.append(min_delay)

    return sorted_delays
