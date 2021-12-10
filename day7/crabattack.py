def calculate_fuel(crab_locations,move_location):
	fuel = 0
	for crab in crab_locations:
		fuel += max(crab,move_location) - min(crab,move_location)
	return fuel

with open('input.txt') as f:
	crab_locations = [int(crab) for crab in f.read().split(',')]
	min_fuel = 9999999
	for i in range(0,max(crab_locations)):
		fuel = calculate_fuel(crab_locations,i)
		if fuel < min_fuel:
			min_fuel = fuel
	print(min_fuel)
