import os
from functools import reduce
import random

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

for path in ["adjectives", "nouns"]:
	for filename in listdir_fullpath(path):
		with open(filename) as old:
			for line in old:
				if len(line.strip().split( ' ')) > 1:
					continue
				else:
					print(line.lower())
