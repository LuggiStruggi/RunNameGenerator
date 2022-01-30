import os
from functools import reduce
import random

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]


adjectives = reduce(lambda x, y : x+y, [[line.strip() for line in open(filename)] for filename in listdir_fullpath("adjectives")])
nouns = reduce(lambda x, y : x+y, [[line.strip() for line in open(filename)] for filename in listdir_fullpath("nouns")])
print(random.choice(adjectives) + " " + random.choice(nouns))

def generate():
	pass
