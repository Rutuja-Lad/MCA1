# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 16:42:49 2023

@author: srushti
"""
import pymongo

client=pymongo.MongoClient("mongodb://localhost:27017/")

db=client["Demo"]
mycol=db["Emp"]

for x in mycol.find():
    print(x)
