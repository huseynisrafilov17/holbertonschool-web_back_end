#!/usr/bin/env python3
"""List all"""


def list_all(mongo_collection):
    return mongo_collection.find()
