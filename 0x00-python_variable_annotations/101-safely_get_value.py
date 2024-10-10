#!/usr/bin/env python3
"""
This module provides a utility function to safely retrieve a value from a
dictionary, with an optional default if the key is not found.
"""

from typing import TypeVar, Mapping, Any, Optional, Union

T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any],
                     key: Any,
                     default: Optional[T] = None) -> Union[Any, T]:
    """
    Safely retrieves a value from a dictionary.

    Args:
        dct (Mapping[Any, Any]): The dictionary to search.
        key (Any): The key to look up in the dictionary.
        default (Optional[T]): A default value to return if the key is not

    Returns:
        Union[Any, T]: The value corresponding to the key, or the default if
        the key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
