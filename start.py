import requests
import utility

origin = "1.469351,103.768997"
# "1.439851,-103.770906"#"San+Francisco"
destination = "1.436032,103.772169"

origins = [origin, destination]
destinations = [destination, origin]

utility.pp_json(utility.get_travel_time_by_location(origins, destinations))