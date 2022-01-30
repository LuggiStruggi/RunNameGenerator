import os
from functools import reduce
import random

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

for path in ["adjectives", "nouns"]:
	for filename in listdir_fullpath(path):
		words = [line.lower() for line in open(filename) if len(line.strip().split(" ")) == 1]
		with open(filename, 'w') as new:
			new.writelines(sorted(words))
