# RunNameGenerator
A simple name generator in the syle of **\<adjective\> \<noun\>** like **mad zebra**.

## Install:

Install using `pip install runnamegen`

## Use:

In python file just
```python
from runnamegen import generate
```
Then in file use
```python
generate()
```
which return a string.

## Commands

There are some commands:

`randnamegen generate` generate runname and display in terminal.

`randnamegen exclude <noun_category>` excludes specific noun-category such as pokemon.

`randnamegen include <noun_category>` includes specific noun-category such as pokemon. 

`randnamegen add-nouns <filename>` adds noun file. Needs to be .txt where each word is seperated by a line break. 

`randnamegen add-adjectives <filename>` adds adjective file. Needs to be .txt where each word is seperated by a line break.

`randnamegen cleanup` cleans up the files such that there are no words which are two words and all are lowercase.

## Source

I got the current set words from https://github.com/gambolputty/textstelle.

## Content

If there are any nouns or adjectives in the current list which you find harmful please create a  [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) for deleting this word.
