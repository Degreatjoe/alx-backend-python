#!/usr/bin/env python3
"""
This module defines an asynchronous generator that yields random numbers
between 0 and 10, 10 times, with a 1-second wait between each yield.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Asynchronously generates random numbers between 0 and 10.
    Loops 10 times, each time waiting 1 second before yielding.

    Yields:
        float: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Wait for 1 second
        yield random.uniform(0, 10)  # Yield a random float between 0 and 10
