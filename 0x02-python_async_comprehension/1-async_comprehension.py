#!/usr/bin/env python3
"""
the module is for asyc oroject
"""
import asyncio
from typing import List
from random import uniform


async def async_generator():
    """Yields random floats asynchronously."""
    for _ in range(10):
        await asyncio.sleep(1)
        yield uniform(0, 10)


async def async_comprehension() -> List[float]:
    """Collects 10 random numbers from async_generator and returns them."""
    return [i async for i in async_generator()]
