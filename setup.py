from setuptools import setup, find_packages
from run_name_generator import __version__

setup(
    name='run_name_generator',
    version=__version__,

    url='https://github.com/LuggiStruggi/RunNameGenerator.git',
    author='Lukas König',
    author_email='lukasmkoenig@gmx.net',

    packages=find_packages(),

	entry_points={
    	'console_scripts': [
        	'runnamegen=run_name_generator.commands:cmd_main',
    	],
	},
)
