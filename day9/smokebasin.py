with open('input.txt') as f:
	grid = [[int(i) for i in list(line.rstrip('\n'))] for line in open("input.txt", "r").readlines()]
	height_level = 0
	for row_id,row in enumerate(grid):
		for col_id,column in enumerate(row):
			found_numbers = []
			for ver in range(-1,2):
				for her in range(-1,2):
					if 0 <= row_id+ver < len(grid) and 0 <= col_id+her < len(grid[0]):
						found_numbers.append(grid[row_id+ver][col_id+her])
			if column == min(found_numbers):	
				height_level += 1 + column
	print(height_level)