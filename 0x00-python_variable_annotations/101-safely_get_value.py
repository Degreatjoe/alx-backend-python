#!/usr/bin/env python3
"""
the function annotation
"""
from typing import TypeVar, Mapping, Any, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping[Any, Any], key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    the corrected annotated function
    """
    if key in dct:
        return dct[key]
    else:
        return default
