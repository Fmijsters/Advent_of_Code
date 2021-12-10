import numpy as np
with open('input.txt') as f:
	input_lines= [line.rstrip() for line in f.readlines()]
	counter = 0
	answers = [2,3,4,7]
	for line in input_lines:
		answer_part_array = line.split(' | ')[1].split(' ')
		for part in answer_part_array:
			if len(part) in answers:
				counter+=1
	print(counter)
	