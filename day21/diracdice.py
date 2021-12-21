with open('input.txt') as f:
	player1,player2 = [[int(starting) for starting in line.split(': ')[-1]] for line in f.read().split('\n')[:2]]
	player1,player2 = player1[0],player2[0]
	turn = 1
	die = 0
	player1_score= 0
	player2_score= 0
	steps=0
	while True:
		rolls= []
		for i in range(3):
			die +=1
			if die >100:
				die = 1
			rolls.append(die)
			steps+=1 

		if turn == 1:
			player1 += sum(rolls)
			while player1 > 10:
				player1-=10
			player1_score+=player1
			if player1_score>=1000:
				break

		if turn == 0:
			player2 += sum(rolls)
			while player2 > 10:
				player2-=10
			player2_score+=player2
			if player2_score>=1000:
				break
		print(turn)
		print('die',rolls)
		print('1',player1,player1_score)
		print('2',player2,player2_score)
		print()

		turn = 0 if turn==1 else 1
	print(steps)
	print(steps*min(player1_score,player2_score))