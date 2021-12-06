import numpy as np
from collections import Counter
with open('input.txt') as f:
	lines = f.readlines()
	binary_input = np.array([list(line.rstrip()) for line in lines])
	gamma =''
	epsilon =''
	for column in range(len(binary_input[0])):
		counted_binary = Counter(binary_input[:,column])
		if counted_binary['0'] > counted_binary['1']:
			gamma += '0'
			epsilon += '1'
		else:
			gamma += '1'
			epsilon += '0'
	print(int(gamma, 2))
	print(int(epsilon, 2))
	print(int(gamma, 2) * int(epsilon, 2))
