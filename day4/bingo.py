import numpy as np



def check_bingo(bingo_cards):
	for bingo_card_id,bingo_mask in enumerate(bingo_cards):
		# print('\n')
		for bingo_single_mask in bingo_mask:
			# print(bingo_single_mask)
			if np.all(bingo_single_mask): 
				print('Bingoooo')
				return True,bingo_card_id
		for bingo_single_mask in np.asarray(bingo_mask).T:
			if np.all(bingo_single_mask):
				print('Bingoooo')
				return True,bingo_card_id
	return False,-1

with open('input.txt') as f:
	lines = f.readlines()
	number_input = [int(number) for number in lines[0].rstrip().split(',')]
	# print(number_input)
	bingo_bords_raw = lines[2:]
	# print(bingo_bords)
	bingo_bord =[]
	bingo_bord_mask =[]
	bingo_bords =[]
	bingo_bords_mask =[]
	for bord_line in bingo_bords_raw:
		if bord_line != "\n":
			bingo_bord.append([int(number) for number in bord_line.rstrip().split(" ") if number!=''])
			bingo_bord_mask.append([False for number in bord_line.rstrip().split(" ") if number!=''])
		else:
			bingo_bords.append(bingo_bord)
			bingo_bords_mask.append(bingo_bord_mask)
			bingo_bord = []
			bingo_bord_mask =[]

			# print(bingo_bords)
			# break
	# print(bingo_bords)

	for number in number_input:
		# number = 76
		for bord_id,bingo_bord in enumerate(bingo_bords):
			for line_id,bingo_line in enumerate(bingo_bord):
				for number_id,bingo_number in enumerate(bingo_line):
					if bingo_number == number:
						bingo_bords_mask[bord_id][line_id][number_id] = True
		found_bingo,card_id = check_bingo(bingo_bords_mask)
		if found_bingo:
			print(sum(np.asarray(bingo_bords)[card_id][np.invert(np.asarray(bingo_bords_mask[card_id]))])*number)
			exit()
		# break
	