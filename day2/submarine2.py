import numpy as np
with open('input.txt') as f:
	lines = [line.strip() for line in f.readlines()]
	directions = [(line.split(' ')[0],int(line.split(' ')[1])) for line in lines]
	direction_dict = {"forward":np.array([1,0,0]),
						"up":np.array([0,0,-1]),
						"down":np.array([0,0,1])}
			# horizontal,depth,aim			
	position = np.zeros(3)
	for direction,distance in directions:
		movement_vector = direction_dict[direction] * distance
		position = np.add(position,movement_vector)
		position[1] += position[2] * distance * int(movement_vector[0]!=0)
	print(np.prod(position[:2]))

	# 1251263225.0
