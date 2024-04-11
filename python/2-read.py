#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *

# try samples of fetching single multiple records with find({})

# Get a single record - in natural order
get_one = restaurants.find_one()
print(dumps(get_one, indent=2))

# Get a specific record set by property
get_another = restaurants.find_one({"borough": "Brooklyn"})
print(dumps(get_another, indent=2))

# # Get several based on a property and count
get_more = restaurants.count_documents({"borough": "Brooklyn"})
print(get_more, "restaurants in Brooklyn")