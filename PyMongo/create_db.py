import pymongo
import bson
import datetime

my_client = pymongo.MongoClient('mongodb://localhost:27017')

# create db
my_db = my_client['mydatabase']

# create collection
my_col = my_db['customers']

# insert document to collection

# mydict = {"name": "John", "address": "Highway 37"}
# x = my_col.insert_one(mydict)
# print(x)

# insert many documents to collection
# my_list = [
#   { "name": "Amy", "address": "Apple st 652", 'age': 40},
#   { "name": "Hannah", "address": "Mountain 21", 'age': 67}
#   ]
# x = my_col.insert_many(my_list)
# print(x.inserted_ids)

# insert document with your own id - remember id must by unique
# mydict = {"_id": 1001, "name": "Ann", "address": "Warsaw"}
# x = my_col.insert_one(mydict)
# print(x.inserted_id)

# find first document in collection
# x = my_col.find_one()
# print(x)

# find all documents in collection
# for x in my_col.find():
#     print(x)

# set which field in result: 1: include, 0: exclude
# for x in my_col.find({},{ "_id": 1, "name": 0 }):
#     print(x)


# filter result - finding condition
# myquery = { "address": "Warsaw" }
# mydoc = my_col.find(myquery)
# for doc in mydoc:
#     print(doc)


# filter result - advanced condition
# myquery = { "address": {"$lt": "S"}}
# mydoc = my_col.find(myquery)
# for doc in mydoc:
#     print(doc)

# filter result - regular expressions
# myquery = { "address": {"$regex": "^W"}, "name": {"$regex": "^W"}}
# mydoc = my_col.find(myquery)
# for doc in mydoc:
#     print(doc)

# myquery = {}
# mydoc = my_col.find(myquery)
# for doc in mydoc:
#     if isinstance(doc['_id'], bson.objectid.ObjectId):
#         print(doc['_id'].generation_time)

gen_time = datetime.datetime(2020, 1, 30, 20, 14)

limit_id = bson.ObjectId.from_datetime(gen_time)

# print(limit_id)

myquery = {"_id": {"$gt": limit_id}}

my_docs = my_col.find(myquery)
for doc in my_docs:
    print(doc)