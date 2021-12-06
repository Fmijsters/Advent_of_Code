with open('./input.txt') as f:
	lines = f.readlines()
	measurements = []
	for line in lines:
		measurements.append(int(line))

	increases = 0
	previous_sum = 0
	for point_index in range(len(measurements)-2):
		current_sum = measurements[point_index]+measurements[point_index+1]+measurements[point_index+2]
		if previous_sum!=0:
			if previous_sum < current_sum:
				increases+=1
		previous_sum = current_sum

	print(increases)

