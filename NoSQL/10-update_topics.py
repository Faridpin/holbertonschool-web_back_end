#!/usr/bin/env python3
''' change all topics '''


def update_topics(mongo_collection, name, topics):
    ''' function '''
    mongo_collection.update_many({"name": name}, {"$set": {"topics": topics}})
