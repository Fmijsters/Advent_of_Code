import numpy as np
with open('input.txt') as f:
	lines = [line.strip() for line in f.readlines()]
	directions = [(line.split(' ')[0],int(line.split(' ')[1])) for line in lines]
	direction_dict = {"forward":np.array([1,0]),
						"up":np.array([0,-1]),
						"down":np.array([0,1])}
	position = np.zeros(2)
	for direction,distance in directions:
		position = np.add(position,direction_dict[direction] *distance)
	print(np.prod(position))