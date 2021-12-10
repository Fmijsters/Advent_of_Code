import numpy as np
with open('input.txt') as f:
	input_lines = [line.rstrip() for line in f.readlines()]
	grid = np.zeros((len(input_lines),len(input_lines[0])))
	for row,line in enumerate(input_lines):
		for column,number in enumerate(line):
			number= int(number)
			grid[row][column] = number
	height_level = 0
	for row_id,row in enumerate(grid):
		for col_id,column in enumerate(row):
			found_numbers = []
			for ver in range(-1,2):
				for her in range(-1,2):
					if 0 <= row_id+ver < len(grid):
						if 0 <= col_id+her < len(grid[0]):
							found_numbers.append(grid[row_id+ver][col_id+her])
			if column == min(found_numbers):	
				height_level += 1 + column
	print(height_level)

