#!/usr/bin/env python3
"""Inserting item to mongodb"""


def insert_school(mongo_collection, **kwargs):
    """Inserts an item"""
    obj = mongo_collection.insert_one(**kwargs)
    return obj.inserted_id
