import numpy as np
from collections import Counter

def filter_canditates(canditates,search_value,column):
	if len(canditates) ==1:
		return canditates
	for c_id in range(len(canditates)-1,-1,-1):
		if canditates[c_id][column] != search_value:
			canditates = np.delete(canditates, c_id, 0)
	return canditates
oxygen_test = ''
co2_test = ''
with open('input.txt') as f:
	lines = f.readlines()
	binary_input = np.array([list(line.rstrip()) for line in lines])
	oxy_canditates=binary_input
	co2_canditates=binary_input
	for column in range(len(binary_input[0])):
		counted_binary_co2 = Counter(co2_canditates[:,column])
		counted_binary_oxy = Counter(oxy_canditates[:,column])
		search_value_co2 = str(int(not counted_binary_co2['0'] <= counted_binary_co2['1']))
		search_value_oxy = str(int(not counted_binary_oxy['0'] > counted_binary_oxy['1']))
		co2_canditates = filter_canditates(co2_canditates,search_value_co2,column)
		oxy_canditates = filter_canditates(oxy_canditates,search_value_oxy,column)

co2 = int(''.join(co2_canditates[0]),2)
oxygen = int(''.join(oxy_canditates[0]),2)
print(co2,oxygen)
print(co2*oxygen)