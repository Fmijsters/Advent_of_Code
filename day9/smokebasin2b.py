import numpy as np

def find_basin2(lowest_point,grid):
	found_values=[lowest_point]
	values_to_check = [lowest_point]
	iters= 0
	while len(values_to_check) != 0:
		to_check,y,x = values_to_check.pop()
		for i,delta in enumerate([-1,-1,1,1]):
			new_x,new_y =x,y
			if i%2==1:
				new_x = x + delta
			else:
				new_y = y + delta
			if not(0<=new_y<len(grid) and 0<=new_x<len(grid[0])):continue
			num_check = grid[new_y][new_x]
			if num_check > to_check and num_check!=9:
				new_low = (num_check,new_y,new_x)
				if new_low not in found_values:
					found_values.append(new_low)
					values_to_check.append(new_low)	
	return found_values

with open('input.txt') as f:
	input_lines = [line.rstrip() for line in f.readlines()]
	grid = np.zeros((len(input_lines),len(input_lines[0])))
	for row,line in enumerate(input_lines):
		for column,number in enumerate(line):
			number = int(number)
			grid[row][column] = number
	lowest_points=[]
	for row_id,row in enumerate(grid):
		for col_id,column in enumerate(row):
			found_numbers = []
			for ver in range(-1,2):
				for her in range(-1,2):
					if 0 <= row_id+ver < len(grid):
						if 0 <= col_id+her < len(grid[0]):
							found_numbers.append(grid[row_id+ver][col_id+her])
			if column == min(found_numbers):
				lowest_points.append((column,row_id,col_id))
	results =[]
	for lowest_point in lowest_points:
		results.append(len(find_basin2(lowest_point,grid)))
	top_3_idx = np.argsort(results)[-3:]
	top_3_values = [results[i] for i in top_3_idx]
	print(np.prod(top_3_values))