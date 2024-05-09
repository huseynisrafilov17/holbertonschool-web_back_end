#!/usr/bin/env python3
"""List all"""


def list_all(mongo_collection):
    """Lists every item in colletion"""
    return mongo_collection.find()
