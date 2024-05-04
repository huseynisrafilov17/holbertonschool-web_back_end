#!/usr/bin/env python3
"""Async"""
import asyncio
import random


async def wait_random(max_delay=10):
    a = random.uniform(0, max_delay)
    await asyncio.sleep(a)
    return a
