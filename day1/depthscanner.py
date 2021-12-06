with open('./input.txt') as f:
	lines = f.readlines()
	measurements = []
	for line in lines:
		measurements.append(int(line))

	increases = 0
	for point_index in range(1,len(measurements)):
		if measurements[point_index-1] < measurements[point_index]:
			increases+=1
			
	print(increases)

