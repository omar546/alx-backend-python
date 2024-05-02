#!/usr/bin/env python3
""" Let's duck type an iterable object"""
from typing import Mapping, Sequence, Iterable, List, Tuple, MutableMapping,


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Element len """
    return [(i, len(i)) for i in lst]
