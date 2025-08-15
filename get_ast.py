from ast import parse, dump
from sys import argv

file = open(argv[1])
tree = parse(file.read())
print(dump(tree, indent=2))