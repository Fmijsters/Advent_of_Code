import numpy as np
from collections import Counter

def generate_paths(paths,nodeToNodes):
	new_paths = []
	for path in paths:
		if path[-1] != 'end':
			for node in nodeToNodes[path[-1]]:
				

				contains_double_lowers= False
				for k,v in Counter(path).items():
					# if path == ['start', 'A', 'b', 'A', 'b']:
					# 	print(k,k==k.lower(), v>=2, node in path)
					if k == k.lower() and v >= 2 and node in path and node == node.lower():
						contains_double_lowers= True
				if node is not path[-1] and not contains_double_lowers:
					new_paths.append(path.copy())
					new_paths[-1].append(node)
	# print()
	# for np in new_paths:
		# print(np)
	return new_paths



nodeToNodes = dict() 
with open('input.txt') as f:
	all_nodes = {}
	# print(innn)
	paths=[]
	input_lines = [line.rstrip() for line in f.readlines()]
	for line in input_lines:
		splitted = line.split('-')
		from_node = splitted[0]
		end_node = splitted[1]
		if end_node != 'start':
			if from_node not in nodeToNodes:
				nodeToNodes[from_node] = [end_node]
			else:
				nodeToNodes[from_node].append(end_node)

		if end_node not in nodeToNodes:
			if from_node != 'start' and end_node!='end':
				nodeToNodes[end_node] = [from_node]
		else:
			if from_node != 'start' and end_node!='end':
				nodeToNodes[end_node].append(from_node)
	# print(nodeToNodes)
	paths.extend([['start',node] for node in nodeToNodes['start']])
	# print(paths)	
	final_paths = []
	old_paths = []
	# print(nodeToNodes)
	while old_paths != paths:
		old_paths = paths
		paths = generate_paths(paths,nodeToNodes)
		for p in paths:
			if p[-1] == 'end':
				final_paths.append(p)

	print(len(final_paths))
	# for p in final_paths:
		# print(p)
		