with open('input.txt') as f:
	lines = [line.rstrip() for line in f.readlines()]
	opening_chars = ['[','<','{','(']
	closing_cars = [']','>','}',')']
	walking_line = []
	errors = []
	score_list = []
	for line in lines:
		inputs = list(line)
		syntaxerror = False
		for inp in inputs:
			if inp in opening_chars:
				walking_line.append(inp)
			else:
				if closing_cars.index(inp) == opening_chars.index(walking_line[-1]):
					del walking_line[-1]
				else:
					errors.append(inp)
					syntaxerror = True
					break
		if not syntaxerror:
			solution = []
			for i_w in range(len(walking_line)-1,-1,-1):
				solution.append(closing_cars[opening_chars.index(walking_line[i_w])])
			score = 0
			for err in solution:
				score *= 5
				if err == ']':
					score+=2
				elif err == ')':
					score+=1
				elif err == '>':
					score+=4
				elif err == '}':
					score+=3
			score_list.append(score)
		walking_line=[]
	score_list.sort()
	print(score_list[len(score_list)//2])