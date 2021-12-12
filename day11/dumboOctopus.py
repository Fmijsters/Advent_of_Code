import numpy as np



with open('input.txt') as f:
	grid  = np.asarray([[int(inp) for inp in list(line.rstrip())] for line in f.readlines()])
	flashes = 0
	for step in range(100):
		# print(grid)
		grid = grid + 1
		# print(grid)
		count = np.count_nonzero(grid > 9)
		to_zero = list()
		while count > 0:
			for row_id,row in enumerate(grid):
				for col_id,number in enumerate(row):
					if grid[row_id][col_id] > 9:
						to_zero.append((row_id,col_id))
						for ver in range(-1,2):
							for hor in range(-1,2):
								if 0<=row_id+ver<len(grid) and 0<=col_id+hor <len(grid[0]) and not(row_id==row_id+ver and col_id==col_id+hor):
									grid[row_id+ver][col_id+hor] +=1

		
			holder_grid= grid
			for tz in to_zero:
				holder_grid[tz[0]][tz[1]] = 0
			count = np.count_nonzero(holder_grid > 9)
			# print(grid)
			# print()

		flashes += len(to_zero)
		for tz in to_zero:
			grid[tz[0]][tz[1]] = 0
		# print(grid)
	print(grid)
	print(flashes)
	# print(grid)




