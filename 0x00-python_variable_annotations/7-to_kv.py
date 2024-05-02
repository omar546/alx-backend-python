#!/usr/bin/env python3
""" Complex types - string & int/float -> tuple"""
from typing import Callable, Union, Optional, List, Tuple, Iterator


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    input string and int OR float
    returns tuple.
    """

    return (k, v**2)
