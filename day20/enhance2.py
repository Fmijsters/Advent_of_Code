from collections import defaultdict
import numpy as np
from scipy import ndimage
import copy
import itertools

def locations(coord):
	# if coord[0]>2 and coord[0]<
	grid = [(-1,-1),(-1,0),(-1,1),
			(0,-1), (0,0), (0,1),
			(1,-1), (1,0), (1,1)]
	points =[] 
	for transmutation in grid:
		points.append((coord[0]+transmutation[0],coord[1]+transmutation[1]))
	return points



def enchance(grid):
	replace = 0 if grid[0, 0] == 1 else 1
	old = np.copy(grid)
	grid[::, 0] = replace
	grid[::, -1] = replace
	grid[0, ::] = replace
	grid[-1, ::] = replace
	
	# to_check = list(itertools.product([-1, 0, 1], [-1, 0, 1]))

	for i in range(1,len(grid)-1):
		for j in range(1,len(grid)-1):
			coord_to_check = (i,j)
			bin_string = ''
			search_grid = locations(coord_to_check)
			for search_coord in search_grid:
				token = old[search_coord[0]][search_coord[1]]
				bin_string += '1' if token == 1 else '0'
			index = int(bin_string,2)
			grid[i][j] = int(algo[index]=='#')


with open('input.txt') as f:
	input_lines = [line.rstrip() for line in f.readlines()]
	image = input_lines[2:]
	# grid = np.empty([300, 300], dtype=np.dtype('str'))
	# grid.fill('.')
	grid = np.zeros((300,300))
	algo = input_lines[0]
	grid2 =[]
	for i in range(len(image)):
		# print(len(image))
		grid2.append([int(j=='#') for j in image[i]])
	grid[100:200, 100:200] = np.asarray(grid2)
	# grid = np.pad(np.asarray(grid),10)
	counter = 0

	# for g in grid:
	# 	l = ''
	# 	for h in g:
	# 		l += h
	# 	print(l)
	# exit(1)
	for i in range(2):
		print(i)
		enchance(grid)
	# enchance(grid)
	# enhance_image(grid)
	# enhance_image(grid)
		
	counter= 0
	for g in grid:
		l = ''
		for h in g:
			counter+= h
		# print(l)
	print(counter)