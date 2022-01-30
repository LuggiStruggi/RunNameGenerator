import os
from functools import reduce
import random

__version__ = '1.0'

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def relative_path(d):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), d)

def generate():
	excludes = [relative_path(os.path.join("nouns", line.strip()+".txt")) for line in open(relative_path("excludes.txt"))]
	adjectives = reduce(lambda x, y : x+y, [[line.strip() for line in open(filename)] for filename in listdir_fullpath(relative_path("adjectives"))])
	nouns = reduce(lambda x, y : x+y, [[line.strip() for line in open(filename)] for filename in listdir_fullpath(relative_path("nouns")) if filename not in excludes])
	return random.choice(adjectives) + " " + random.choice(nouns)
