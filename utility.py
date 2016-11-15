import json
import requests

# AIzaSyCZt4IGG8XFtgZRnre6URzBkKQHZpnUyKY
# https://maps.googleapis.com/maps/api/distancematrix/json?origins=Seattle&destinations=San+Francisco&mode=driving&language=en-US&key=AIzaSyCZt4IGG8XFtgZRnre6URzBkKQHZpnUyKY

google_keys = "AIzaSyCZt4IGG8XFtgZRnre6URzBkKQHZpnUyKY"
baseurl = "https://maps.googleapis.com/maps/api/distancematrix/json?"
language = "en-US"
mode = "driving"

def pp_json(json_thing, sort=True, indents=4):
    if type(json_thing) is str:
        print(json.dumps(json.loads(json_thing), sort_keys=sort, indent=indents))
    else:
        print(json.dumps(json_thing, sort_keys=sort, indent=indents))
    return None

def get_travel_time_by_location(origins, destinations):
	in_origin = ""
	in_destination = ""
	for origin in origins:
		in_origin = in_origin + "|" + origin
	for destination in destinations:
		in_destination = in_destination + "|" + destination
	print in_origin[1:]
	print in_destination[1:]
	url = baseurl + "&origins="+in_origin+"&destinations="+in_destination+"&mode="+mode+"&language="+language+"&key="+google_keys
	return requests.get(url).json()