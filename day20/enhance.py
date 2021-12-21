from collections import defaultdict
import numpy as np
from scipy import ndimage
def locations(coord):
	grid = [(-1,-1),(-1,0),(-1,1),
			(0,-1), (0,0), (0,1),
			(1,-1), (1,0), (1,1)]
	points =[]
	for transmutation in grid:
		points.append((coord[0]+transmutation[0],coord[1]+transmutation[1]))
	return points





with open('input.txt') as f:
	input_lines = [line.rstrip() for line in f.readlines()]
	# print(input_lines)
	image = input_lines[2:]
	algo = input_lines[0]
	print(algo)
	print()
	image_dict= defaultdict(lambda:0)
	grid =[]
	for i in range(len(image)):
		grid.append([int(j=='#') for j in image[i]])
		for j in range(len(image[i])):
		# 	# row.append(int(image[i][j]=='#'))
			if image[i][j] == '#':
				image_dict[(i,j)] = 1
		# grid.append(row)
	for a in range(2):
		min_x = min([k[1] for k in list(image_dict.keys())])
		min_y = min([k[0] for k in list(image_dict.keys())])
		max_x = max([k[1] for k in list(image_dict.keys())])
		max_y = max([k[0] for k in list(image_dict.keys())])
		new_image_dict= defaultdict(lambda:0)
		grid =[]
		for i in range(min_y-2,max_y+3):
			row = []
			for j in range(min_x-2,max_x+3):
				checking_coord = (i,j)
				key = ''
				search_grid = locations(checking_coord)
				for search_coord in search_grid:
					key += str(image_dict[search_coord])
				if algo[int(key,2)] == '#':
					new_image_dict[checking_coord] = 1
				row.append(algo[int(key,2)])
			grid.append(row)
		image_dict = new_image_dict
	

	grid= np.asarray(grid)[2:-2, 2:-2]

	counter=0
	for row in grid:
		line=''
		for l in row:
			line+=l
			counter += int(l=='#')
		# print(''.join(grid))
		print(line)

	print(counter)
