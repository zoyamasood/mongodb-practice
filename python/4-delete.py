#!/usr/bin/env python3

from pymongo import MongoClient, errors
from bson.json_util import dumps
import os
from db import *


# Deletes first one it finds matching criteria


# Or delete ALL documents found matching criteria
# restaurants.delete_many()

get_record = restaurants.find({"name":"Mama Gina's Classy Kitchen"})
print(dumps(get_record, indent=2))