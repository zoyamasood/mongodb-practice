#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *

get_record = restaurants.find({"name":"Mama Gina's Classy Kitchen"})
print(dumps(get_record, indent=2))

# Deletes first one it finds matching criteria
restaurants.delete_one({"name":"Mama Gina's Classy Kitchen"})

# Deletes all documents found matching criteria
# restaurants.delete_many()
