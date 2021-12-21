import math
def explode(snailfish,depth=1,stop=False,direction_rest=None,floating_rest=None,s_print=False):
	if type(snailfish) == list:
		if type(snailfish[0]) == list and type(snailfish[1]) == list:
			print(depth,"both lists",snailfish)
			flr = None
			drr = None
			for i,lil_snailfish in enumerate(snailfish):
				if i == 1:
					if drr == 1:
						if s_print:
							print('flipped direction')
						drr = 0
					elif drr == 0:
						print('removed rest',drr,flr)
						drr = None
						flr = None
				if s_print:
					# print('here',floating_rest,direction_rest,stop,lil_snailfish)
				# if lil_snailfish == [1,1]:
					print(depth,drr,flr,'Here',floating_rest,direction_rest,stop,lil_snailfish,snailfish[0])
				_,flr,drr,stop = explode(lil_snailfish,depth+1,stop,drr,flr,s_print)
				# if s_print:
					# print('HERE',depth,flr,drr,stop,lil_snailfish)
				# if i == 1 and direction_rest == 0 and stop != False:
				# 	direction_rest = 1
				# 	print("WAKE UP NEED TO GO TO LEFT SIDE",floating_rest)
				# 	_,floating_rest,direction_rest,stop = explode(lil_snailfish,depth+1,stop,direction_rest,floating_rest,s_print)

		elif type(snailfish[0]) == int and type(snailfish[1]) == list:
			if direction_rest == 0 and floating_rest:
				if s_print:
					print('Used floating',direction_rest,floating_rest)
				snailfish[0] += floating_rest
				floating_rest = None
				direction_rest = None
				
			explosion, floating, direction, stop = explode(snailfish[1],depth+1,stop,direction_rest,floating_rest,s_print)
			if s_print:
				print(depth,'right',direction,floating,floating_rest,direction_rest,snailfish[0],snailfish[1])
				# print('right',floating_rest,direction_rest,snailfish[0],snailfish[1])
			if direction == 0 and floating:
				snailfish[0] += floating
				floating= None
			
			if explosion == True:
				snailfish[0]+=snailfish[1][0]
				floating = snailfish[1][1]
				snailfish[1] = 0

			return snailfish,floating,1,stop


		elif type(snailfish[0]) == list and type(snailfish[1]) == int:
			if direction_rest == 1 and floating_rest:
				if s_print:
					print('Used floating',direction_rest,floating_rest)
				snailfish[1] += floating_rest
				floating_rest = None
				direction_rest = None
			explosion,floating,direction,stop = explode(snailfish[0],depth+1,stop,direction_rest,floating_rest,s_print)
			if s_print:
				print(depth,'left',floating_rest,direction_rest,snailfish[1],snailfish[0])
				# print('left',explosion,floating,floating_rest,direction_rest,snailfish[1],snailfish[0])

			if direction == 1 and floating:
				snailfish[1] += floating
				floating= None

			if explosion == True:
				snailfish[1]+=snailfish[0][1]
				floating = snailfish[0][0]
				snailfish[0] = 0
				# stop=True
				# print(snailfish)
			return snailfish,floating,0,stop

		else:
			# print(depth,'both numbers',snailfish[0],snailfish[1])
			if depth > 4 and not stop:
				# print('should explode',snailfish)
				return True,-1,-1,True
	else:
		# print(most_left,most_right,snailfish,depth,[],[])
		pass
	return snailfish,None,None,None

def split(snailfish,stop=False):
	if type(snailfish) == list:
		if type(snailfish[0]) == list and type(snailfish[1]) == list:
			# print(depth,"both lists")
			floating_rest = None
			direction_rest = None
			for i,lil_snailfish in enumerate(snailfish):
				stop = split(lil_snailfish,stop)
		elif type(snailfish[0]) == int and type(snailfish[1]) == list:
			if snailfish[0] > 9:
				snailfish[0] = [snailfish[0]//2,math.ceil(snailfish[0]/2)]
				return True
			stop = split(snailfish[1],stop)
			
		elif type(snailfish[0]) == list and type(snailfish[1]) == int:
			if snailfish[1] > 9:
				snailfish[1] = [snailfish[1]//2,math.ceil(snailfish[1]/2)]
				return True
			stop = split(snailfish[0],stop)
			
		else:
			if snailfish[0] > 9:
				snailfish[0] = [snailfish[0]//2,math.ceil(snailfish[0]/2)]
				return True
			if snailfish[1] > 9:
				snailfish[1] = [snailfish[1]//2,math.ceil(snailfish[1]/2)]
				return True
	else:
		pass
	return snailfish



# result,_,_,_ = explode([[[[[9,8],1],2],3],4])
# print(result == [[[[0,9],2],3],4])

# print()
# result,_,_,_ = explode([7,[6,[5,[4,[3,2]]]]])
# print(result == [7,[6,[5,[7,0]]]])

# print()
# result,_,_,_ = explode([[6,[5,[4,[3,2]]]],1])
# print(result == [[6,[5,[7,0]]],3])


# print()
# result,_,_,_ = explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
# print(result == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])

# print()
# result,_,_,_ = explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
# print(result == [[3,[2,[8,0]]],[9,[5,[7,0]]]])

# print()
# result = split([[[0,7],4],[15,[0,13]]])
# print(result == [[[0,7],4],[[7,8],[0,13]]])

# print()
# result = split([[[0,7],4],[[7,8],[0,13]]])
# print(result == [[[0,7],4],[[7,8],[0,[6,7]]]])

print()
a = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
# print(a)
a,_,_,_ = explode(a)
# print(a)
# print([[[[0,7],4],[7,[[8,4],9]]],[1,1]])
# print(a==[[[[0,7],4],[7,[[8,4],9]]],[1,1]])
# print()
a,_,_,_ = explode(a)
# print(a)
# print(a==[[[[0,7],4],[15,[0,13]]],[1,1]])

print()
a = split(a)
# print(a)
# print(a==[[[[0,7],4],[[7,8],[0,13]]],[1,1]])

a = split(a)
# print(a)
# print([[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]])
print(a)
a,_,_,_ = explode(a,s_print=True)
print(a)
print([[[[0,7],4],[[7,8],[6,0]]],[8,1]])