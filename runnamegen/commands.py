import os
import json
from runnamegen import generate

def listdir_fullpath(d):
    return [os.path.join(d, f) for f in os.listdir(d)]

def relative_path(d):
	return os.path.join(os.path.dirname(os.path.abspath(__file__)), d)

def exclude_choices():
	possible = [os.path.splitext(filename)[0] for filename in os.listdir(relative_path("nouns"))]
	return [category for category in possible if category not in include_choices()]

def cmd_exclude(category):
	category = category.lower()+"\n"
	excludes = [line.lower() for line in open(relative_path("excludes.txt"))]
	if category not in excludes:
		excludes.append(category)
	with open(relative_path("excludes.txt"), 'w') as new:
		new.writelines(sorted(excludes))

def change_config(name, state):
	with open(relative_path('config.json')) as f:
		config = json.load(f)
	config[name] = state
	with open(relative_path('config.json'), 'w') as f:
		json.dump(config, f)

def read_config(name):
	with open(relative_path('config.json')) as f:
		config = json.load(f)[name]
	return config

def increment_alphabet():
	with open(relative_path('config.json')) as f:
		config = json.load(f)
	if config["alphabet"] == "":
		return
	elif config["alphabet"] == "z":
		config["alphabet"] = "a"
	else:	
		config["alphabet"] = chr(ord(config["alphabet"][0]) + 1)
	with open(relative_path('config.json'), 'w') as f:
		json.dump(config, f)

def include_choices():
	return [line.strip().lower() for line in open(relative_path("excludes.txt"))]

def cmd_include(category):
	category = category.lower()+"\n"
	with open('config.json') as f:
		excludes = [e.lower() for e in json.load(f)["excludes"]]
	if category not in excludes:
		return
	excludes.remove(category)
	with open(relative_path("excludes.txt"), 'w') as new:
		new.writelines(sorted(excludes))

def cmd_generate(delimiter: str = " "):
	print(generate(delimiter))

def delete_word_from_file(word, filename):
	with open(filename) as f:
		words = [line.lower() for line in f if line.lower() != word and line.lower() != word+"\n"]
	with open(filename, 'w') as new:
		new.writelines(sorted(words))

def handle_duplicates(previous_words: dict, current_words: list, filename: str) -> dict:
	for w in current_words:
		if w in previous_words:
			done = False
			inpt = input(f"File [1]: {os.path.splitext(os.path.basename(previous_words[w]))[0]} and\n"+
                         f"File [2]: {os.path.splitext(os.path.basename(filename))[0]} share the word {w}.\n"+
						 f"Would you like the word removed from [1], [2] or leave it in both [3]?")
			while not done:
				if inpt == "1":
					delete_word_from_file(w, previous_words[w])
					done = True
				elif inpt == "2":
					current_words.remove(w)
					done = True
				elif inpt == "3":
					done = True
				else:
					inpt = input("Type either 1, 2 or 3.")
					done = False
		else:
			previous_words[w] = filename

	return previous_words, current_words

def cmd_cleanup():
	for path in ["adjectives", "nouns"]:
		prev_words = {}
		for filename in listdir_fullpath(relative_path(path)):
			with open(filename) as f:
				words = [line.lower() for line in f if len(line.strip().split(" ")) == 1]
			words = list(set(words))
			prev_words, words = handle_duplicates(previous_words=prev_words, current_words=words, filename=filename)
			with open(filename, 'w') as new:
				new.writelines(sorted(words))

def cmd_add_nouns(filename):
	noun_dir = relative_path("nouns")
	os.rename(filename, os.path.join(noun_dir, os.path.basename(filename)))

def cmd_add_adjectives(filename):
	noun_dir = relative_path("adjectives")
	os.rename(filename, os.path.join(noun_dir, os.path.basename(filename)))

def cmd_main():
	import argparse
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest='subcommand')	

	p_exclude = subparsers.add_parser('exclude')
	p_exclude.add_argument('category', type=str, choices=exclude_choices(), help='exclude noun-category from randnamegen')

	p_include = subparsers.add_parser('include')
	p_include.add_argument('category', type=str, choices=include_choices(), help='include noun-category to randnamegen')
	
	p_add_nouns = subparsers.add_parser('add-nouns')
	p_add_nouns.add_argument('filename', type=str, help='add noun file to randnamegen')

	p_add_adj = subparsers.add_parser('add-adjectives')
	p_add_adj.add_argument('filename', type=str, help='add adjective file to randnamegen')

	p_generate = subparsers.add_parser('generate', help='generate run name')
	p_generate.add_argument('delimiter', type=str, choices=[' ', '_', '-'], help='change the delimiter', nargs='?', default=" ")
	p_generate.add_argument('-n', type=int, help='number of random words', default=1)
	
	p_cleanup = subparsers.add_parser('cleanup', help='clean up word files (remove 2 word words and lowercase)')

	p_alphabet = subparsers.add_parser('alphabet', help='alphabet mode')
	p_alphabet.add_argument('mode', type=str, choices=['on', 'off'], help='alphabet mode on or off')
	
	p_alliteration = subparsers.add_parser('alliteration', help='alliteration mode')
	p_alliteration.add_argument('mode', type=str, choices=['on', 'off'], help='alliteration mode on or off')

	args = parser.parse_args()

	if args.subcommand == "exclude":
		cmd_exclude(args.category)
	elif args.subcommand == "include":
		cmd_include(args.category)
	elif args.subcommand == "add-nouns":
		cmd_add_nouns(args.filename)
	elif args.subcommand == "add-adjectives":
		cmd_add_nouns(args.filename)
	elif args.subcommand == "generate":
		[(cmd_generate(args.delimiter), increment_alphabet()) for i in range(args.n)]
	elif args.subcommand == "cleanup":
		cmd_cleanup()
	elif args.subcommand == "alliteration":
		if args.mode == "on":
			change_config("alliteration", True)
		elif args.mode == "off":
			change_config("alliteration", False)
	elif args.subcommand == "alphabet":
		if args.mode == "on":
			change_config("alphabet", "a")
		elif args.mode == "off":
			change_config("alphabet", "")
