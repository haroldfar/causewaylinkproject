import pymongo
from pymongo import MongoClient
client = MongoClient("localhost", 27017)
db = client["pokemon"]
result = db.pokemon.find({})
for r in result:
	print r