# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:44:19 2023

@author: srushti
"""

import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client["Demo"]
mycol=db["Emp"]

for x in mycol.find_one():
    print(x)