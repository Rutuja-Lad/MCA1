# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 14:59:53 2023

@author: Ganesh
"""

import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017/')
data=client['database']
col=data['fruit']
mylist={'name':'gvava'}
newvalue={'$set':{'test':'soure'}}
       
x=col.update_one(mylist,newvalue)
print(x)