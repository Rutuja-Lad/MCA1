# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:17:09 2023

@author: srushti
"""

import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client["Demo"]
mycol=db["Emp"]

mydict={"name":"srushti","address":"kolhapur"}

mycol.insert_one(mydict)

for x in mycol.find():
 print(x)