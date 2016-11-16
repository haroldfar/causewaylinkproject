import requests
import utility
import json
from db import api

origin = "1.469351,103.768997"
# "1.439851,-103.770906"#"San+Francisco"
destination = "1.436032,103.772169"

origins = [origin, destination]
destinations = [destination, origin]

dbapi = api.MONGO_API()
for item in dbapi.get_all_records():
	# utility.pp_json(item)
	print item


# utility.pp_json(utility.get_travel_time_by_location(origins, destinations))