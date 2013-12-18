import shelve

def main():

	db = shelve.open("Jo.db")
	print db["Jo"]

	print "\n\n"

	print len(db["Jo"])

	for x in db["Jo"]:
		print x, "\n"

if __name__ == "__main__":
	main()
