with open('input.txt') as f:
	lines = [line.rstrip() for line in f.readlines()]
	opening_chars = ['[','<','{','(']
	closing_cars = [']','>','}',')']
	walking_line = []
	errors = []
	for line in lines:
		inputs = list(line)
		for inp in inputs:
			if inp in opening_chars:
				walking_line.append(inp)
			else:
				if closing_cars.index(inp) == opening_chars.index(walking_line[-1]):
					del walking_line[-1]
				else:
					errors.append(inp)
					break
		walking_line=[]
	error_score = 0
	for err in errors:
		if err == ']':
			error_score+=57
		elif err == ')':
			error_score+=3
		elif err == '>':
			error_score+=25137
		elif err == '}':
			error_score+=1197
	print(error_score)