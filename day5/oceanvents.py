import numpy as np
from collections import Counter
with open('input.txt') as f:
	line_input = [line.rstrip().split(' -> ') for line in f.readlines()]
	line_coordinates = []
	for line in line_input:
		start_point = line[0]
		end_point = line[1]
		start_point = [int(coord) for coord in start_point.split(',')]
		end_point = [int(coord) for coord in end_point.split(',')]
		line_coordinates.append((start_point,end_point))

	grid = np.zeros((1000,1000))
	for line_coord in line_coordinates:
		start_point,end_point = line_coord
		x1,y1 = start_point
		x2,y2 = end_point
		if x1 == x2:
			for y3 in range(min(y1,y2),max(y1,y2)+1):
				grid[y3][x1] +=1
		elif y1 == y2:
			for x3 in range(min(x1,x2),max(x1,x2)+1):
				grid[y1][x3] +=1
		else:
			x = x1
			y = y1
			grid[y][x] +=1
			while x != x2 and y != y2:
				if x1 < x2:
					x +=1
				if x1 > x2:
					x -=1
				if y1 < y2:
					y +=1
				if y1 > y2:
					y -=1
				grid[y][x] +=1
				
	unique, counts = np.unique(grid, return_counts=True)
	count_dict = dict(zip(unique, counts))
	print(count_dict[2.0]+count_dict[3.0]+count_dict[4.0]+count_dict[5.0])



