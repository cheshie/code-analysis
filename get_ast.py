from ast import parse, dump
from sys import argv
from astpretty import pprint

file = open(argv[1])
tree = parse(file.read())
print(pprint(tree, indent=2))