import pymongo
from pymongo import MongoClient

def get_db(db_name):
	hostname = "localhost"
	port_number = 27017
	client = MongoClient(hostname, port_number)
	return client[db_name]
