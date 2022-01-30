import os
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
	possible = [os.path.splitext(filename)[0]+"\n" for filename in os.listdir(relative_path("nouns"))]
	if category not in possible:
		return
	excludes = [line.lower() for line in open(relative_path("excludes.txt"))]
	if category not in excludes:
		excludes.append(category)
	with open(relative_path("excludes.txt"), 'w') as new:
		new.writelines(sorted(excludes))

def include_choices():
	return [line.strip().lower() for line in open(relative_path("excludes.txt"))]

def cmd_include(category):
	category = category.lower()+"\n"
	excludes = [line.lower() for line in open(relative_path("excludes.txt"))]
	if category not in excludes:
		return
	excludes.remove(category)
	with open(relative_path("excludes.txt"), 'w') as new:
		new.writelines(sorted(excludes))

def cmd_generate(delimiter: str=" "):
	print(generate(delimiter))

def cmd_cleanup():
	for path in ["adjectives", "nouns"]:
		for filename in listdir_fullpath(relative_path(path)):
			words = [line.lower() for line in open(filename) if len(line.strip().split(" ")) == 1]
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
	
	p_cleanup = subparsers.add_parser('cleanup', help='clean up word files (remove 2 word words and lowercase)')
	
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
		cmd_generate(args.delimiter)
	elif args.subcommand == "cleanup":
		cmd_cleanup()
