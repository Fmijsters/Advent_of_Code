import math
import copy
def explode(snailfish,depth=1,stop=False,dir_r=None,flt_r=None,s_print=False,my_side=-1):
	# if s_print:
	# print(snailfish,flt_r,dir_r,stop,my_side)
	if type(snailfish) == list:
		if type(snailfish[0]) == list and type(snailfish[1]) == list:
			for i,lil_snailfish in enumerate(snailfish):
				explosion,flt_r,dir_r,stop,big_problem = explode(lil_snailfish,depth+1,stop,dir_r,flt_r,s_print,i)
				if explosion==True:
					if s_print:
						print('list explosion',i,explosion,depth,flt_r,dir_r,snailfish)
					if i == 0:
						snailfish[1][0] += snailfish[0][1]
						flt_r = snailfish[0][0]
						snailfish[0] = 0
						dir_r = 0
					if i == 1:
						snailfish[0][1] += snailfish[1][0]
						flt_r = snailfish[1][1]
						snailfish[1] = 0
						dir_r = 1
					if s_print:
						print('resulted in',snailfish,dir_r,flt_r)
				if big_problem and not explosion==True:
					if s_print:
						print("BIG FUCKING PROBLEM")
					if dir_r == 0:
						dir_r = 1
					else:
						dir_r = 0
					holder= snailfish[0]
					while type(holder) == list:
						if type(holder[dir_r]) == int:
							holder[dir_r] += flt_r
							flt_r = None
							dir_r = None
							break
						holder = holder[dir_r]
				elif i == 1 and dir_r == 0 and stop == True and my_side==1:
					return snailfish,flt_r,dir_r,stop,True
			return snailfish,flt_r,dir_r,stop,False


		elif type(snailfish[0]) == int and type(snailfish[1]) == list:
			if dir_r == 0 and flt_r:
				if s_print:
					print('Used floating',dir_r,flt_r)
				snailfish[0] += flt_r
				flt_r = None
				dir_r = None
				
			explosion, flt_r, dir_r, stop,_ = explode(snailfish[1],depth+1,stop,dir_r,flt_r,s_print,1)

			if dir_r == 0 and flt_r:
				if s_print:
					print('Used floating')
				snailfish[0] += flt_r
				flt_r= None
				dir_r = None
			
			if explosion == True:
				if s_print:
					print('\tin explode',snailfish)
				snailfish[0]+=snailfish[1][0]
				flt_r = snailfish[1][1]
				snailfish[1] = 0
				dir_r = 1
				if s_print:
					print("\tresulted in",snailfish)

			# if s_print:
			# 	print(depth,'right',flt_r,dir_r,snailfish)
			return snailfish,flt_r,dir_r,stop,False
		elif type(snailfish[0]) == list and type(snailfish[1]) == int:
			print('left')
			if dir_r == 1 and flt_r:
				if s_print:
					print('Used floating',dir_r,flt_r)
				snailfish[1] += flt_r
				flt_r = None
				dir_r = None

			explosion,flt_r,dir_r,stop,_ = explode(snailfish[0],depth+1,stop,dir_r,flt_r,s_print,0)
			if dir_r == 1 and flt_r:
				if s_print:
					print('Used floating')
				snailfish[1] += flt_r
				flt_r = None
				dir_r = None

			if explosion == True:
				if s_print:
					print('\tin explode',snailfish)
				snailfish[1]+=snailfish[0][1]
				flt_r = snailfish[0][0]
				snailfish[0] = 0
				dir_r = 0
				if s_print:
					print("\tresulted in",snailfish)
			return snailfish,flt_r,dir_r,stop,False

		else:
			if s_print:
				print(dir_r,my_side,flt_r)
			if stop and flt_r and dir_r == my_side:
				if dir_r == 1 and dir_r == my_side:
					print('im here',snailfish,dir_r,my_side)
				elif dir_r == 0:
					print('im here',snailfish,dir_r,my_side)
				if s_print:
					print('\tin numbers',snailfish)
				if dir_r==1:
					dir_r=0
				snailfish[dir_r] += flt_r
				flt_r = None
				dir_r = None
				if s_print:
					print('\tresulted in',snailfish)
				

			if depth > 4 and not stop:
				if s_print:
					print('should explode',snailfish)
				return True,None,None,True,False
			return snailfish,flt_r,dir_r,stop,False
	else:
		return snailfish,flt_r,dir_r,stop,False
	return snailfish,None,None,stop,False

def split(snailfish,stop=False):
	if type(snailfish) == list:
		if type(snailfish[0]) == list and type(snailfish[1]) == list:
			# print(depth,"both lists")
			flt_r = None
			dir_r = None
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

def reduce(snailfish):
	new_snailfish = None
	counter = 0
	while new_snailfish != snailfish:
		while new_snailfish != snailfish:
			if new_snailfish:
				snailfish = new_snailfish
			new_snailfish,_,_,_,_ = explode(copy.deepcopy(snailfish),s_print=counter == 3)
			print('input',new_snailfish)
			print()
			print()
			counter += 1
			if counter ==4:
				exit()
			# print(new_snailfish)
		if new_snailfish:
			snailfish = new_snailfish	
		new_snailfish = split(copy.deepcopy(snailfish))
	return new_snailfish
# print("DONE",new_snailfish)



# print(reduce([[[[[9,8],1],2],3],4]) == [[[[0,9],2],3],4])
# print(reduce([7,[6,[5,[4,[3,2]]]]]) == [7,[6,[5,[7,0]]]])
# print(reduce([[6,[5,[4,[3,2]]]],1]) == [[6,[5,[7,0]]],3])
# result,_,_,_ = explode([[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]])
# print(result == [[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
# result,_,_,_ = explode([[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]])
# print(result == [[3,[2,[8,0]]],[9,[5,[7,0]]]])
# a = [[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]
# print(reduce(a) == [[[[0,7],4],[[7,8],[6,0]]],[8,1]])


# result,_,_,_ = explode([[[[[1, 1], [2, 2]], [3, 3]], [4, 4]], [5, 5]],s_print=False)
# print(result)
# result,_,_,_ = explode(result)
# print(result)

with open('input.txt') as f:
	previous_result= None
	input_list = [eval(line.rstrip()) for line in f.readlines()]
	# print(input_list)
	for i_id in range(1,len(input_list)):
		added = None
		if not previous_result:
			added = [input_list[i_id-1],input_list[i_id]]
			print()
			print(added)
			previous_result = reduce(copy.deepcopy(added))
		else:
			added = [previous_result,input_list[i_id]]
			previous_result =  reduce(copy.deepcopy(added))
	print(previous_result)
	print(previous_result == [[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]])
	# print([[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]])

# [[[[0, [4, 5]], [0, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
# [[[[4, 0], [5, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]

# [[[[4, 0], [5, 0]], [[[4, 5], [2, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]
# [[[[4, 0], [5, 4]], [[0, [7, 6]], [9, 5]]], [7, [[[3, 7], [4, 3]], [[6, 3], [8, 8]]]]]

