with open('input.txt') as f:
	input_ages = [int(age) for age in f.readlines()[0].rstrip().split(',')]
	ages = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
	for i_age in input_ages:
		ages[i_age]+=1
	for i in range(256):
		new_ages = {0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0}
		previous_ages = 0
		for age in range(len(ages)):
			if age == 0:
				new_ages[8] = ages[age]
				new_ages[6] = ages[age]
			else:
				new_ages[age-1] += ages[age]
		ages = new_ages

print(sum(ages.values()))	