"""
Saying generator
"""

import shelve, random

def say_it():
	
	db = shelve.open("Jo.db")
	she_said = db["Jo"][random.randint(0, len(db["Jo"]))]
	
	db.close()
	return she_said

if __name__ == "__main__":
	
	print "\n"
	print say_it()
	print "\n"
