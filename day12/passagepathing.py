import numpy as np
from collections import defaultdict

# print(input_lines)
# Python program to print all paths from a source to destination.

def main(): 
	nodeToNodes = dict() 
	with open('input.txt') as f:
		all_nodes = {}
		innn = f.read().split('\n\n')
		# print(innn)
		input_lines = [line.rstrip() for line in innn[0].split('\n')]
		liness = innn[1]
		for line in input_lines:
			splitted = line.split('-')
			from_node = splitted[0]
			end_node = splitted[1]
			if from_node not in nodeToNodes:
				if end_node != 'start':
					nodeToNodes[from_node] = [end_node]
			else:
				if end_node != 'start':
					nodeToNodes[from_node].append(end_node)
			if end_node not in nodeToNodes:
				if from_node != 'start' and end_node!='end':
					nodeToNodes[end_node] = [from_node]
			else:
				if from_node != 'start'and end_node!='end':
					nodeToNodes[end_node].append(from_node)
		print(nodeToNodes)

		print(len(getAllSimplePaths('start', 'end', nodeToNodes)))


def getAllSimplePaths(originNode, targetNode, nodeToNodes): 
	return helpGetAllSimplePaths(targetNode, 
								 [originNode], 
								 set([originNode]), 
								 defaultdict(lambda: 0),
								 nodeToNodes, 
								 list())  

def helpGetAllSimplePaths(targetNode, 
						  currentPath, 
						  usedNodes,
						  usedNodesCount, 
						  nodeToNodes, 
						  answerPaths): 
	print(currentPath,dict(usedNodesCount))
	lastNode = currentPath[-1] 
	if lastNode == targetNode: 
		answerPaths.append(list(currentPath)) 
	else: 
		for neighbor in nodeToNodes[lastNode]: 
			if neighbor not in usedNodes: 
				currentPath.append(neighbor) 
				if neighbor == neighbor.lower():
					usedNodesCount[neighbor] += 1
					count = np.count_nonzero(np.asarray(list(usedNodesCount.values())) >= 2)
					if count >= 1:
						usedNodes.add(neighbor) 
				helpGetAllSimplePaths(targetNode, 
									  currentPath, 
									  usedNodes, 
									  usedNodesCount.copy(),
									  nodeToNodes, 
									  answerPaths) 
				if neighbor == neighbor.lower():
					count = np.count_nonzero(np.asarray(list(usedNodesCount.values())) >= 2)
					if count >= 1:
						usedNodes.remove(neighbor) 
				currentPath.pop() 
	return answerPaths 
 
if __name__ == '__main__': 
	main() 



