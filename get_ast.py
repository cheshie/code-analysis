from ast import parse
from astpretty import pprint
from sys import argv

file = open(argv[1])
tree = parse(file.read())
pprint(tree)
