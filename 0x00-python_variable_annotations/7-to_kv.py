#!/usr/bin/env python3
from typing import Union, Tuple
"""
tthe annotated function
"""


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    the annotated function
    """
    return (k, float(v ** 2))
