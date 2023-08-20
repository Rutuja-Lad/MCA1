# -*- coding: utf-8 -*-
import pymongo
client=pymongo.MongoClient('mongodb://localhost:27017/')
db=client['mydb']
mycol=db['employee']
mydict={'name':'pooja','address':'pune'}
x=mycol.insert_one(mydict)
print(x)


