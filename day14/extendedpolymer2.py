import numpy as np
from collections import Counter
from collections import defaultdict
with open('input.txt') as f:
	polymer,rules = f.read().split('\n\n')
	polymer = polymer.rstrip()
	rule_dict = dict()
	for rule in rules.split('\n'):
		key,value= rule.split(' -> ')
		rule_dict[key] = value
	steps = 40
	bigrams=defaultdict(lambda:0)
	letter_count = defaultdict(lambda:0)

	for k, v in Counter(polymer).items():
		letter_count[k] = v

	for k, v in Counter([''.join(item) for item in list(zip(polymer[::1],polymer[1::]))]).items():
		bigrams[k] = v
	for step in range(steps):
		to_add=defaultdict(lambda:0)
		for letters,insertion in rule_dict.items():
			if letters in bigrams:
				letter_count[insertion] += bigrams[letters]
				to_add[letters[0] + insertion] += bigrams[letters]
				to_add[insertion + letters[1]] += bigrams[letters]
				bigrams[letters] = 0	

		for k,v in to_add.items():	
			bigrams[k] += v
				

	print(max(letter_count.values())-min(letter_count.values()))
