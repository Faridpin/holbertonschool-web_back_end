#!/usr/bin/env python3
''' return all docs'''


def list_all(mongo_collection):
    ''' function '''
    return list(mongo_collection.find())
