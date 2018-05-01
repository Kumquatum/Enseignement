#!/usr/bin/env python

import json
import os.path
from collections import defaultdict

# recursive, non-blocking tree structure
def tree():
   return defaultdict(tree)

# recursive builder
def apply(tree, value):
   # return tree if not value else apply(tree[value.pop()], value) 
   if not value:
       return tree
   else:
       first = value.pop()
       apply(tree[first], value)

# file parser
def build_tree(filename):
	with open(filename) as f:
		# tree structure
		x = tree()
		for line in f:
			apply(x, line.strip().split(".")[::-1])
	return json.loads(json.dumps(x))

if __name__ == "__main__":
	# dot-separated tree file
	tree_filename = os.path.join(os.path.abspath('.'), 'otu_map.txt')
	# build it
	my_tree = build_tree(tree_filename)

	print(my_tree)