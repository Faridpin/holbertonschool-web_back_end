#!/usr/bin/env python3
''' add a new collection '''


def insert_school(mongo_collection, **kwargs):
    ''' function '''
    return mongo_collection.insert_one(kwargs).inserted_id
