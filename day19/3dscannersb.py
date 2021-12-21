from collections import Counter
from itertools import permutations
from scipy.spatial.transform import Rotation as R
from collections import defaultdict
from more_itertools import pairwise
from scipy.spatial.distance import squareform, pdist

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

def generate_points(base_scanner,new_scanner,rotation_id):
	all_points = []
	for point in base_scanner:
		for point2 in new_scanner:
			all_rotations = [x for x in sequence(point2)]
			rotated_point = all_rotations[rotation_id]
			all_points.append(tuple([point[0]+rotated_point[0]*-1,point[1]+rotated_point[1]*-1,point[2]+rotated_point[2]*-1]))
	return all_points


def BFS_SP(graph, start, goal):
    explored = []
    queue = [[start]]
    if start == goal:
        print("Same Node")
        return
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            neighbours = [v[0] for v in graph[node]]
            for neighbour in neighbours:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)
                if neighbour == goal:
                    # print("Shortest path = ", *new_path)
                    return new_path
            explored.append(node)
    print('no path')
    return

def point_location_from_other_pov(base_location,new_location,rotation_id):
	rotation_b = [x for x in sequence(new_location)][rotation_id]
	new_point = [base_location[0]+rotation_b[0],
				 base_location[1]+rotation_b[1],
			 	 base_location[2]+rotation_b[2]]
	return new_point


# print(paths)


def transform_pov_scanner(paths,to_scanner, scanner_id):
    shortest = BFS_SP(paths, to_scanner, scanner_id)
    new_point = None
    rotations = []
    points = []
    for i in range(len(shortest)-2,-1,-1):
        if i < len(shortest)-2:
            rotations.append([p for p in paths[shortest[i]] if p[0] == shortest[i+1]][0][1])
        points.append([p for p in paths[shortest[i]] if p[0] == shortest[i+1]][0][2])
    new_point= None
    for i in range(1,len(points)):
        if not new_point:
            new_point = point_location_from_other_pov(points[i],points[i-1],rotations[i-1])
        else:
            new_point = point_location_from_other_pov(points[i],new_point,rotations[i-1])
    return new_point  

def transform_pov_scan_point(paths,scan,scanner_id,to_scanner):    
    # print('Finding path from',scanner_id,'to',to_scanner)
    shortest = BFS_SP(paths, to_scanner, scanner_id)
    new_point = None
    for i,path in enumerate(pairwise(reversed(shortest))):
        path = list(reversed(path))
        part2= None
        if i == 0:
        	part2 = scan
        else:
        	part2 = new_point
        part1 = [p for p in paths[path[0]] if p[0] == path[1]][0][2]
        rotation = [p for p in paths[path[0]] if p[0] == path[1]][0][1]
        new_point = point_location_from_other_pov(part1,part2,rotation)
    return new_point

import numpy as np

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
		# print(scanner)
	scanners.append(scanner)
	paths = {}
	matches = []
	for i in range(len(scanners)):
		for j in range(len(scanners)):
			if i == j: continue
			for r_id in range(24):
				gen_points = generate_points(scanners[i],scanners[j],r_id)
				counted = Counter(gen_points).most_common()
				if counted[0][1] >= 12:
					matches.append([i,j])	
					if i in paths:
						paths[i].append((j,r_id,counted[0][0]))
					else:
						paths[i] = [(j,r_id,counted[0][0])]
					break

# print(paths)
scanner_locations=[]
for i in paths.keys():
    if i != 0:
        scanner_locations.append(np.asarray(transform_pov_scanner(paths,0,i)))
scanner_locations.insert(0,[0,0,0])
max_dist= 0
for p in paths[0]:
    scanner_locations[p[0]] = np.asarray(p[2])

# print(scanner_locations)
for i,loc in enumerate(scanner_locations):
    for j,loc2 in enumerate(scanner_locations):
        if i == j:continue
        # print(loc,loc2)
        dist = pdist([loc,loc2],'cityblock')
        # print(i,j,dist,loc,loc2)
        if dist > max_dist:
            max_dist = dist
print('maximum distance:',max_dist[0])
# print(transform_pov_scanner(paths))

