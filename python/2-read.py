#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *

# try samples of fetching single multiple records with find({})

# Get a single record - in natural order
get_one = 
print(dumps(get_one, indent=2))

# Get a specific record set by property
get_another = 
print(dumps(get_another, indent=2))

# # Get several based on a property and count
get_more = 
print(get_more, "restaurants in Brooklyn")