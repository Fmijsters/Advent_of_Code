import numpy as np

def find_basin2(lowest_point,grid):
	found_values=[lowest_point]
	values_to_check = [lowest_point]
	iters= 0
	while len(values_to_check) != 0:
		to_check,y,x = values_to_check.pop()
		for x1 in range(x-1,-1,-1):
			num_check = grid[y][x1]
			if num_check == 9:
				break
			if num_check > to_check:
				new_low = (num_check,y,x1)
				if new_low not in found_values:
					found_values.append(new_low)
					values_to_check.append(new_low)
				break
			break
		for x2 in range(x+1,len(grid[0])):
			num_check = grid[y][x2]
			if num_check == 9:
				break
			if num_check > to_check:
				new_low = (num_check,y,x2)
				if new_low not in found_values:
					found_values.append(new_low)
					values_to_check.append(new_low)
				break
			break
		for y1 in range(y-1,-1,-1):
			num_check = grid[y1][x]
			if num_check == 9:
				break
			if num_check > to_check:
				new_low = (num_check,y1,x)
				if new_low not in found_values:
					found_values.append(new_low)
					values_to_check.append(new_low)
				break
			break
		for y2 in range(y+1,len(grid)):
			num_check = grid[y2][x]
			if num_check == 9:
				break
			if num_check > to_check:
				new_low = (num_check,y2,x)
				if new_low not in found_values:
					found_values.append(new_low)
					values_to_check.append(new_low)
				break
			break
	return found_values

with open('input.txt') as f:
	input_lines = [line.rstrip() for line in f.readlines()]
	grid = np.zeros((len(input_lines),len(input_lines[0])))
	for row,line in enumerate(input_lines):
		for column,number in enumerate(line):
			number= int(number)
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