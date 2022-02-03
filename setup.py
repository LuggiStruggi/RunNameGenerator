from setuptools import setup, find_packages
from runnamegen import __version__

setup(	
		name='runnamegen', version=__version__,
		url='https://github.com/LuggiStruggi/RunNameGenerator.git',
		author='Lukas König',
		author_email='lukasmkoenig@gmx.net',
		packages=find_packages(),
		package_data = {'runnamegen' : ['config.json', 'excludes.txt', 'nouns/*', 'adjectives/*']},
		entry_points={'console_scripts': ['runnamegen=runnamegen.commands:cmd_main']},
		decription="A simple run-name generator. Creates names in the style \"<adjective> <noun>\" like \"mad zebra\""
	)
