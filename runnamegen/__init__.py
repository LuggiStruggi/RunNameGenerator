import os
from functools import reduce
import random
import json

__version__ = '1.7.3'

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def relative_path(d):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), d)

def read_config(name):
	with open(relative_path('config.json')) as f:
		config = json.load(f)[name]
	return config

def generate(delimiter: str = " "):
	
	alliteration = read_config("alliteration")
	letter = read_config("alphabet")
	
	excludes = [relative_path(os.path.join("nouns", line.strip()+".txt")) for line in open(relative_path("excludes.txt"))]

	# nouns
	nouns = [[line.strip() for line in open(filename)] for filename in listdir_fullpath(relative_path("nouns")) if filename not in excludes]
	nouns = reduce(lambda x, y : x+y, nouns)
	if nouns == []:
		nouns = ["john-doe"]
	if letter != "":
		nouns = [n for n in nouns if n[0] == letter]
	if nouns == []:
		nouns = ["john-doe"]
	random_noun = random.choice(nouns)
	
	#adjectives
	adjectives = [[line.strip() for line in open(filename)] for filename in listdir_fullpath(relative_path("adjectives"))]
	adjectives = reduce(lambda x, y : x+y, adjectives)
	if adjectives == []:
		adjectives = ["standard"]
	if alliteration:
		adjectives = [a for a in adjectives if a[0] == random_noun[0]]
	if adjectives == []:
		adjectives = ["standard"]

	return random.choice(adjectives) + delimiter + random_noun
