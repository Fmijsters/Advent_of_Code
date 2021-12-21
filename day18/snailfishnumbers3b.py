import math
import copy

def find_rightest_neighbor(total_snailfish,path):
	holder= total_snailfish
	done = False
	for coord in path[:-1]:
		holder = holder[coord]
	value = holder[path[-1]][1]
	reversed_path = list(reversed(path))
	start_building=False
	new_path=[]
	for i in range(0,len(path)):
		if reversed_path[i] == 0 and not start_building:
			start_building = True
			new_path.append(1)
			continue
		if start_building:
			new_path.insert(0,reversed_path[i])
	holder2 = total_snailfish
	for coord in new_path:
		if isinstance(holder2[coord],list):
			holder2 = holder2[coord]
		else:
			holder2[coord] += value
			done = True
	while not done and isinstance(holder2[0],list):
		holder2= holder2[0]
	if not done:
		holder2[0] += value
		done = True
	return total_snailfish,done

def find_leftest_neighbor(total_snailfish,path):
	holder= total_snailfish
	done = False
	for coord in path[:-1]:
		holder = holder[coord]
	value = holder[path[-1]][0]
	reversed_path = list(reversed(path))
	start_building=False
	new_path=[]
	for i in range(0,len(path)):
		if reversed_path[i] == 1 and not start_building:
			start_building = True
			new_path.append(0)
			continue
		if start_building:
			new_path.insert(0,reversed_path[i])
	holder2 = total_snailfish
	for coord in new_path:
		if isinstance(holder2[coord],list):
			holder2 = holder2[coord]
		else:
			holder2[coord] += value
			done = True
	while not done and isinstance(holder2[1],list):
		holder2= holder2[1]
	if not done:
		holder2[1] += value
		done = True
	return total_snailfish,done

def explode(total_snailfish,snailfish,depth=1,path=[]):
	if isinstance(snailfish[0],list) or isinstance(snailfish[1],list):
		for i,lil_snailfish in enumerate(snailfish):
			path_holder= copy.deepcopy(path)
			if isinstance(lil_snailfish,list):
				path_holder.append(i)
				total_snailfish,stop = explode(total_snailfish,lil_snailfish,depth+1,copy.deepcopy(path_holder))
				if stop:
					break
		return total_snailfish,stop
	elif depth>4:
		most_left= False
		most_right = False
		done = [False,False]
		if set(path) == set([0]):
			most_left= True
		if set(path) == set([1]):
			most_right = True
		
		holder= total_snailfish
		for coord in path[:-1]:
			holder = holder[coord]
		my_neighbour = 0
		if path[-1] == 0: my_neighbour=1
		if isinstance(holder[my_neighbour],int):
			holder[my_neighbour] += holder[path[-1]][my_neighbour]
			done[my_neighbour] = True
		
		if done[0]:
			pass
		elif not most_left:
			total_snailfish,done[0] = find_leftest_neighbor(total_snailfish,path)
		if done[1]:
			pass
		elif not most_right:
			total_snailfish,done[1] = find_rightest_neighbor(total_snailfish,path)
		holder[path[-1]] = 0
		return total_snailfish,True

	else:
		return total_snailfish,False
	return total_snailfish,False

def split(snailfish,stop=False):
	if type(snailfish) == list:
		if type(snailfish[0]) == list and type(snailfish[1]) == list:
			for i,lil_snailfish in enumerate(snailfish):
				_,stop = split(lil_snailfish,stop)
			return snailfish,stop
		elif type(snailfish[0]) == int and type(snailfish[1]) == list:
			if snailfish[0] > 9 and not stop:
				snailfish[0] = [snailfish[0]//2,math.ceil(snailfish[0]/2)]
				stop = True
			_,stop = split(snailfish[1],stop)
			return snailfish,stop
		elif type(snailfish[0]) == list and type(snailfish[1]) == int:
			_,stop = split(snailfish[0],stop)
			if snailfish[1] > 9 and not stop:
				snailfish[1] = [snailfish[1]//2,math.ceil(snailfish[1]/2)]
				stop = True
			return snailfish, stop
		else:
			if snailfish[0] > 9 and not stop:
				snailfish[0] = [snailfish[0]//2,math.ceil(snailfish[0]/2)]
				stop = True
			if snailfish[1] > 9 and not stop:
				snailfish[1] = [snailfish[1]//2,math.ceil(snailfish[1]/2)]
				stop = True
			return snailfish, stop
	else:
		return snailfish, stop
	return snailfish, stop

def reduce(snailfish):
	new_snailfish = None
	counter = 0
	while new_snailfish != snailfish:
		while new_snailfish != snailfish:
			if new_snailfish:
				snailfish = new_snailfish
			new_snailfish,_ = explode(copy.deepcopy(snailfish),copy.deepcopy(snailfish),path=[])
			if new_snailfish != snailfish:
				pass
				# print("after explode:\t",new_snailfish)
		if new_snailfish:
			snailfish = new_snailfish	
		new_snailfish,_ = split(copy.deepcopy(snailfish))
		if new_snailfish != snailfish:
			pass
			# print("after split:\t",new_snailfish)
	return new_snailfish

def mag(snailfish):
	if type(snailfish) == list:
		if type(snailfish[0]) == list and type(snailfish[1]) == list:
			magnitudes=[]
			for i,lil_snailfish in enumerate(snailfish):
				magnitude = mag(lil_snailfish)
				magnitudes.append(magnitude)
			# print(magnitudes)
			return magnitudes[0] *3 + magnitudes[1]*2

		elif type(snailfish[0]) == int and type(snailfish[1]) == list:
			magnitude = mag(snailfish[1])
			magnitude = snailfish[0] * 3 + magnitude*2
			return magnitude

		elif type(snailfish[0]) == list and type(snailfish[1]) == int:
			magnitude = mag(snailfish[0])
			magnitude = magnitude*3 + snailfish[1] * 2
			return magnitude

		else:
			magnitude = snailfish[0]*3 + snailfish[1]*2
			return magnitude

	else:
		return magnitude
	return magnitude

with open('input.txt') as f:
	# previous_result= None
	highest_mag = 0
	input_list = [eval(line.rstrip()) for line in f.readlines()]
	for i,x in enumerate(input_list):
		print(i)
		for j,y in enumerate(input_list):
			if i != j:
				reduced = reduce(copy.deepcopy([x,y]))
				print([x,y])
				print(reduced)
				magnitude = mag(reduced)
				print(magnitude)
				if magnitude>highest_mag:

					highest_mag = magnitude
	print(highest_mag)

# print(reduce([[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]], [[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]]))
