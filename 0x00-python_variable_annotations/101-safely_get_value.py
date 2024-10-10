#!/usr/bin/env python3
"""
Function annotation example
"""
from typing import TypeVar, Mapping, Any, Optional, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any],
                     key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    A function that safely retrieves a value from a dictionary.
    If the key is not found, it returns the default value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
