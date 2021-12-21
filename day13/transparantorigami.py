import numpy as np

with open('input.txt') as f:
	dots,folds = f.read().split('\n\n')
	max_x,max_y = 0,0
	for d in dots.split('\n'):
		x,y = [int(number.rstrip()) for number in d.split(',')]
		if x > max_x:
			max_x = x
		elif y > max_y:
			max_y = y

	grid = np.chararray((max_y+1,max_x+1)).astype(str)
	grid[:]='.'

	for dot in dots.split('\n'):
		x,y = [int(number.rstrip()) for number in dot.split(',')]
		grid[y][x] = '#'
	for fold in folds.split('\n'):
		print(fold)
		if 'y' in fold:
			vertical_fold = int(fold.split('y=')[1])
			grid[vertical_fold] = '-'
			new_part = np.flipud(grid[vertical_fold+1:])
			for i in range(vertical_fold):
				for j in range(len(new_part[i])):
					if new_part[i][j]== '#':
						grid[i][j] = new_part[i][j]
			grid = grid[:vertical_fold]

		elif 'x' in fold:
			horizontal_fold = int(fold.split('x=')[1])
			grid[:,horizontal_fold] = '|'
			new_part = np.fliplr(grid[:,horizontal_fold+1	:])
			for i in range(len(new_part)):
				for j in range(horizontal_fold):
					if new_part[i][j]== '#':
						grid[i][j] = new_part[i][j]
			grid = grid[:,:horizontal_fold]
	for r in grid:
		print(list(r))




	# print(grid)
