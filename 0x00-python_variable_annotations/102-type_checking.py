#!/usr/bin/env python3
"""
the corrected code file
"""
from typing import List, Tuple


def zoom_array(lst: List[int], factor: int = 2) -> List[int]:
    """
    Returns a zoomed-in version of the array, repeating each element
    based on the factor provided.

    Args:
        lst (List[int]): The list to zoom in on.
        factor (int): The factor by which to zoom the list.

    Returns:
        List[int]: A list with elements repeated according to the factor.
    """
    zoomed_in: List[int] = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # Corrected to pass an integer
