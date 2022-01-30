import os
from run_name_generator import generate

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

def cmd_generate():
	print(generate())

def cmd_main():
	import argparse
	parser = argparse.ArgumentParser()
	subparsers = parser.add_subparsers(dest='subcommand')	

	p_exclude = subparsers.add_parser('exclude')
	p_exclude.add_argument('category', type=str, choices=exclude_choices(), help='exclude noun-category from randnamegen')

	p_include = subparsers.add_parser('include')
	p_include.add_argument('category', type=str, choices=include_choices(), help='include-noun category to randnamegen')

	p_generate = subparsers.add_parser('generate', help='generate run name')
	
	args = parser.parse_args()
	if args.subcommand == "exclude":
		cmd_exclude(args.category)
	elif args.subcommand == "include":
		cmd_include(args.category)
	elif args.subcommand == "generate":
		cmd_generate()
