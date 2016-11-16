import database
import datetime

dbname = "causewaylink"

class MONGO_API(object):
	def __init__(self):
		self.db = database.get_db("pokemon")

	def get_all_records(self):
		return self.db["pokemon"].find({})

	def insert_distance_time_record(content):
		return 0
	
	def get_iterator_number(it_name):
		next_no = self.db["iterator"].find({"_id":it_name})
		if next_no:
			return next_no + 1
		else:
			return 0
