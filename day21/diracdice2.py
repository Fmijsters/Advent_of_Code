player1 = 4
player2 = 8
player1_score = 0
player2_score = 0
scores  = [(1,0),(2,0)]
players = [(1,4),(2,8)]
stop_score= 13
done = []
# while True:
import itertools
import numpy as np
from functools import lru_cache

@lru_cache(maxsize=None)
def game(location1,player1_score,location2,player2_score,turn):
	if player1_score >= 21:
		return 1,0
	if player2_score >= 21:
		return 0,1
	total_score1= 0
	total_score2= 0
	if turn == 1:		
		for a in range(1,4):
			for i in range(1,4):
				for j in range(1,4):
					loc_1 = location1+ a+i+j
					while loc_1 > 10:
						loc_1 -= 10
					p1,p2 = game(loc_1,player1_score+loc_1,location2,player2_score,2)
					total_score1+=p1
					total_score2+=p2

	elif turn == 2:
		for a in range(1,4):
			for i in range(1,4):
				for j in range(1,4):
					loc_2 = location2+ a+i+j
					while loc_2 > 10:
						loc_2 -= 10
					p1,p2 = game(location1,player1_score,loc_2,player2_score+loc_2,1)
					total_score1+=p1
					total_score2+=p2
	return total_score1,total_score2

winners= game(4,0,8,0,1)
print(winners)
# print(dict(zip(unique, counts)))