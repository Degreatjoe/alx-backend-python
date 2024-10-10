#!/usr/bin/env python3
"""
the function annotation
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    the function has been corrected
    """
    if lst:
        return lst[0]
    else:
        return None
