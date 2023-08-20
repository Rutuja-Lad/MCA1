# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:36:06 2023

@author: Ganesh
"""

import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017/')
data=client['database']
col=data['fruit']
x={'name':'gvava'}
s=col.delete_one(x)
for s in col.find():   
 print(s)