
from collections import Counter
with open('input.txt') as f:
	polymer,rules = f.read().split('\n\n')
	polymer = list(polymer.rstrip())
	rule_dict = dict()
	for rule in rules.split('\n'):
		key,value= rule.split(' -> ')
		rule_dict[key] = value
	steps = 10
	for i in range(steps):
		pairs=[]
		to_add= ""
		for p_id in range(len(polymer)):
			if p_id + 2 <= len(polymer):
				pairs.append((polymer[p_id:p_id+2]))
			else:
				to_add = polymer[p_id:p_id+2][0]
		# print(pairs)
		for p_id in range(len(pairs)):
			insert_letter = rule_dict[''.join(pairs[p_id])]
			pairs[p_id].insert(1,insert_letter)
		flat_list = [item for sublist in pairs for item in sublist[:2]]
		polymer = flat_list
		polymer.append(to_add)
		print(len(polymer))
	counted = Counter(polymer).values()
	print(max(counted)-min(counted))

	# print(len(polymer))

