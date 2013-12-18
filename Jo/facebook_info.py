import facebook, shelve

print "Here we go again!"


token = "CAACEdEose0cBAJvVlyE61N5yZC8TZAeCItwIj5T5ZC2BflfbBFFR1A7FZC8JPeuItG2ZASGinIchbN1ZCZCEFdDsmNyJSY8iKoJVE88D6k3LVeZAkfr42kS0qsxRZCr8GSAB2fY2oyL5Poaz5njlg3ZCIIUGOuZCNMbW9VpUrHFRIqV1imYJZBv0KtvK7ZCudlbR3tc8ZD"

Jo_id = "802280014"

graph = facebook.GraphAPI(token)
profile = graph.get_object(Jo_id)
friends = graph.get_connections("me", "friends")

print profile

sayings = []

statuses = graph.get_connections(Jo_id, "statuses", limit=200)

for index, value in enumerate(statuses["data"]):
	print index, value["message"]
	
	sayings.append(value["message"])
	
	print "\n\n"

db = shelve.open("Jo.db")
db["Jo"] = sayings

db.close()

