def calculate_fuel(crab_locations,move_location):
	fuel = 0
	for crab in crab_locations:
		min_value = min(crab,move_location)
		max_value = max(crab,move_location)
		number_of_steps = max_value - min_value + 1
		arithemtic_series = (number_of_steps * ((crab+move_location)-2*min_value))/2
		fuel += arithemtic_series
	return fuel

with open('input.txt') as f:
	crab_locations = [int(crab) for crab in f.read().split(',')]
	min_fuel = 9999999999999
	for i in range(0,max(crab_locations)):
		# i = 5
		fuel = calculate_fuel(crab_locations,i)
		# break
		if fuel < min_fuel:
			min_fuel = fuel
		# break
	print(int(min_fuel))
