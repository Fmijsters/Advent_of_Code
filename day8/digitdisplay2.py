import numpy as np
with open('input.txt') as f:
	input_lines= [line.rstrip() for line in f.readlines()]
	counter = 0
	for line in input_lines:
		clock_input = {1:[],2:[],3:[],4:[],5:[],6:[],7:[]}
		numbers = {0:[],1:[],2:[],3:[],4:[],5:[],6:[],7:[],8:[],9:[]}
		question_part = line.split(' | ')[0]
		question_part_array = [list(word) for word in question_part.split(' ')]
		answer_part = line.split(' | ')[1]
		answer_part_array = [list(word) for word in answer_part.split(' ')]
		letters ={'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[]}
		for k in letters.keys():
			for part in question_part_array:
				if k in part:
					letters[k].append(part)
		# find known numbers
		for part in question_part_array:
			if len(part) == 2:
				numbers[1] = part
			if len(part) == 4:
				numbers[4] = part
			if len(part) == 7:	
				numbers[8] = part
			if len(part) == 3:
				numbers[7] = part 
			
		clock_input[1] = list(set(numbers[7])^set(numbers[1]))[0]
		counts_dict = {}
		for k,v in letters.items():
			if len(v) in counts_dict.keys():
				counts_dict[len(v)].append(k)
			else:
				counts_dict[len(v)] = [k]
		for k,v in letters.items():
			if len(v) == 8 and k in numbers[1] and k in numbers[7]:
				clock_input[2] = k
			if len(v) == 4:
				clock_input[6] = k
			if len(v) == 9:
				clock_input[4] = k
			if len(v) == 7:
				hidden_answer = list(set([''.join(l) for l in letters[counts_dict[len(v)][0]]])^set([''.join(l) for l in letters[counts_dict[len(v)][1]]]))
				for a in hidden_answer:
					if len(a) == 4 and k not in a:
						clock_input[5] = k
						for pos_letter in counts_dict[7]:
							if pos_letter != k:
								clock_input[3] = pos_letter

		all_options = list('abcdefg')
		found = [v for k,v in clock_input.items() if len(v) != 0]
		clock_input[7] = list(set(all_options)^set(found))[0]

		final_number_dict = {}
		number_string = ''.join(sorted(clock_input[1] + clock_input[2] + clock_input[4] + clock_input[5] + clock_input[6] + clock_input[7]))
		final_number_dict[number_string] = 0 
		number_string = ''.join(sorted(clock_input[2] + clock_input[4]))
		final_number_dict[number_string] = 1 
		number_string = ''.join(sorted(clock_input[1] + clock_input[2] + clock_input[3] + clock_input[6] + clock_input[5]))
		final_number_dict[number_string] = 2 
		number_string = ''.join(sorted(clock_input[1] + clock_input[2] + clock_input[3] + clock_input[4] + clock_input[5]))
		final_number_dict[number_string] = 3 
		number_string = ''.join(sorted(clock_input[7] + clock_input[3] + clock_input[2] + clock_input[4]))
		final_number_dict[number_string] = 4 
		number_string = ''.join(sorted(clock_input[1] + clock_input[7] + clock_input[3] + clock_input[4] + clock_input[5]))
		final_number_dict[number_string] = 5 
		number_string = ''.join(sorted(clock_input[1] + clock_input[7] + clock_input[3] + clock_input[4] + clock_input[5] + clock_input[6]))
		final_number_dict[number_string] = 6 
		number_string = ''.join(sorted(clock_input[1] + clock_input[2] + clock_input[4]))
		final_number_dict[number_string] = 7 
		number_string = ''.join(sorted(clock_input[1] + clock_input[2] + clock_input[3] + clock_input[4] + clock_input[5] + clock_input[6] + clock_input[7]))
		final_number_dict[number_string] = 8 
		number_string = ''.join(sorted(clock_input[1] + clock_input[2] + clock_input[3] + clock_input[4] + clock_input[5] + clock_input[7]))
		final_number_dict[number_string] = 9
		decoded = ''
		for answer in answer_part_array:
			decoded+=str(final_number_dict[''.join(sorted(answer))])
		counter += int(decoded)
	print(counter)

