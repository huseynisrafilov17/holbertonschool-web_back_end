#!/usr/bin/env python3
"""Annotations"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    total = 0
    for i in mxd_lst:
        total += i
    return total
