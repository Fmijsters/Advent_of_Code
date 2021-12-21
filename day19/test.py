import numpy as np
from math import cos,sin
from scipy.spatial.transform import Rotation as R
from itertools import permutations

def roll(v): return (v[0],v[2],-v[1])
def turn(v): return (-v[1],v[0],v[2])
def sequence (v):
    for cycle in range(2):
        for step in range(3):  # Yield RTTT 3 times
            v = roll(v)
            yield(v)           #    Yield R
            for i in range(3): #    Yield TTT
                v = turn(v)
                yield(v)
        v = roll(turn(roll(v)))  # Do RTR


# 0 -> 1
a = (68, -1246, -43)
# 1 -> 4
b = (686,422,578)
rotation_b = [x for x in sequence(b)][16] # rotation from 0 -> 1
new_point = [a[0]+rotation_b[0], #+ b[0]*rotation_a[0],
			 a[1]+rotation_b[1], #+ b[1]*rotation_a[1],
			 a[2]+rotation_b[2]] #
print([-20,-1133,1061])
print(new_point)







print()
# 0 -> 1
a = (68, -1246, -43)

# 1 -> 3
b = (160, -1134, -23)
rotation_b = [x for x in sequence(b)][16] # rotation from 0 -> 1
new_point = [a[0]+rotation_b[0], #+ b[0]*rotation_a[0],
			 a[1]+rotation_b[1], #+ b[1]*rotation_a[1],
			 a[2]+rotation_b[2]] #
print([-92,-2380,-20])
print(new_point)

def point_location_from_other_pov(base_location,new_location,rotation_id):
	# print(base_location)
	# print(new_location)
	# print(rotation_id)
	rotation_b = [x for x in sequence(new_location)][rotation_id]
	new_point = [base_location[0]+rotation_b[0],
				 base_location[1]+rotation_b[1],
			 	 base_location[2]+rotation_b[2]]
	return new_point

def find_all_paths(paths,from_node,to_node,combinations):
	# print(paths[from_node])
	for node in paths[from_node]:
		if node in combinations:
			continue
		combinations.append(node)
		if node == to_node:
			return
		find_all_paths(paths,node,to_node,combinations)

		# print(node)


paths = {0: [1], 1: [0, 3, 4], 2: [4], 3: [1], 4: [1, 2]}
combinations =[0]
find_all_paths(paths,0,1,combinations)
print(combinations)
# for values in paths[1][1:]:
# 	# print(values)
# 	# for v in values:
# 	print(values[0],point_location_from_other_pov(paths[0][0][2],values[2],paths[0][0][1]))
	# break




# 0 -> 1
a = (68, -1246, -43) # 3
# 1 -> 4 
b = (88, 113, -1104) # 2
# 4 -> 2 
c = (168, -1125, 72) # 1

rotation_c = [x for x in sequence(c)][20] # rotation from 4 -> 2
new_point = [b[0]+rotation_c[0],
			 b[1]+rotation_c[1],
			 b[2]+rotation_c[2]]
print('used',b,c)
print(new_point)
rotation_c = [x for x in sequence(new_point)][16] # rotation from 4 -> 0 i hope
new_point = [a[0]+rotation_c[0], 
			 a[1]+rotation_c[1],
			 a[2]+rotation_c[2]]
print('used',a)
print(new_point)
print([1105,-1205,1229])



# 727,592,562
# -293,-554,779
# 441,611,-461
# -714,465,-776
# -743,427,-804
# -660,-479,-426
# 832,-632,460
# 927,-485,-438
# 408,393,-506
# 466,436,-512
# 110,16,151
# -258,-428,682
# -393,719,612
# -211,-452,876
# 808,-476,-593
# -575,615,604
# -485,667,467
# -680,325,-822
# -627,-443,-432
# 872,-547,-609
# 833,512,582
# 807,604,487
# 839,-516,451
# 891,-625,532
# -652,-548,-490
# 30,-46,-14

with open('input.txt') as f:
	input_scanners = [line.rstrip() for line in f.readlines()]
	scanners = []
	scanner = []
	for line in input_scanners[1:]:
		if '' == line:
			continue
		if "---" in line:
			scanners.append(scanner)
			scanner= []
			continue
		scanner.append([int(coord) for coord in line.split(',')])
	scanners.append(scanner)
	# print(scanners[4])
	for scan in scanners[4]:
		a = (68, -1246, -43) # 16
		# 1 -> 4
		b = (88, 113, -1104) # 20
		# 4 -> 2
		c = scan

		rotation_c = [x for x in sequence(c)][20] # rotation from 4 -> 2
		new_point = [b[0]+rotation_c[0],
					 b[1]+rotation_c[1],
					 b[2]+rotation_c[2]]
		# print('used',b,c)
		# print(new_point)/
		rotation_c = [x for x in sequence(new_point)][16] # rotation from 4 -> 0 i hope
		new_point = [a[0]+rotation_c[0], 
					 a[1]+rotation_c[1],
					 a[2]+rotation_c[2]]
		# print('used',a)
		print(new_point)
		# print([1105,-1205,1229])	
