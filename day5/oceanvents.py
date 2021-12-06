import numpy as np
from collections import Counter
with open('input.txt') as f:
	line_input = [line.rstrip().split(' -> ') for line in f.readlines()]
	# print(line_input)
	line_coordinates = []
	max_x,max_y = 0,0
	for line in line_input:
		start_point = line[0]
		end_point = line[1]
		start_point = [int(coord) for coord in start_point.split(',')]
		max_x = max(start_point[0],max_x)
		max_y = max(start_point[1],max_y)
		end_point = [int(coord) for coord in end_point.split(',')]
		max_x = max(end_point[0],max_x)
		max_y = max(end_point[1],max_y)
		# if start_point[0] == end_point[0] or start_point[1] == end_point[1]:
		line_coordinates.append((start_point,end_point))

	grid = np.zeros((max_y+1,max_x+1))
	for line_coord in line_coordinates:
		start_point,end_point = line_coord
		x1,y1 = start_point
		x2,y2 = end_point
		print(start_point,end_point)
		if x1 == x2:
			# print("Vertical line")
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
				
	# for line in grid:
	# 	print(line)



			# print("Horizontal line")
		# break
	# for line in grid:
	# 	print(line)
	unique, counts = np.unique(grid, return_counts=True)
	print(dict(zip(unique, counts)))



