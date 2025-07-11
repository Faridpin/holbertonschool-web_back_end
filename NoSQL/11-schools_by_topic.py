#!/usr/bin/env python3
''' list of schools with spesific topic '''


def schools_by_topic(mongo_collection, topic):
    ''' function '''
    return list(mongo_collection.find({"topics": topic}))
