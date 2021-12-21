from collections import defaultdict
from more_itertools import pairwise
import numpy as np
from scipy.spatial.distance import squareform, pdist
# paths = {0: [1], 1: [0, 3, 4], 2: [4], 3: [1], 4: [1, 2]}
paths = {0: [(1, 16, (68, -1246, -43))], 1: [(0, 16, (68, 1246, -43)), (3, 11, (160, -1134, -23)), (4, 20, (88, 113, -1104))], 2: [(4, 19, (1125, -168, 72))], 3: [(1, 11, (-160, 1134, 23))], 4: [(1, 1, (-1104, -88, 113)), (2, 19, (168, -1125, 72))]}
# Function to build the graph
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


def point_location_from_other_pov(base_location,new_location,rotation_id):
    # print(base_location)
    # print(new_location)
    # print(rotation_id)
    rotation_b = [x for x in sequence(new_location)][rotation_id]
    new_point = [base_location[0]+rotation_b[0],
                 base_location[1]+rotation_b[1],
                 base_location[2]+rotation_b[2]]
    return new_point
 
# Driver Code
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

if __name__ == "__main__":
    paths={0: [(1, 16, (68, -1246, -43))], 1: [(0, 16, (68, 1246, -43)), (3, 11, (160, -1134, -23)), (4, 20, (88, 113, -1104))], 2: [(4, 19, (1125, -168, 72))], 3: [(1, 11, (-160, 1134, 23))], 4: [(1, 1, (-1104, -88, 113)), (2, 19, (168, -1125, 72))]}
    scanner_locations= []
    for i in paths.keys():
        if i != 0:
            scanner_locations.append(np.asarray(transform_pov_scanner(paths,0,i)))
    scanner_locations.insert(0,[0,0,0])
    max_dist= 0
    for p in paths[0]:
        scanner_locations[p[0]] = np.asarray(p[2])

    for i,loc in enumerate(scanner_locations):
        for j,loc2 in enumerate(scanner_locations):
            if i == j:continue
            # print(loc,loc2)
            dist = pdist([loc,loc2],'cityblock')
            print(i,j,dist,loc,loc2)
            if dist > max_dist:
                max_dist = dist
    print(max_dist)
        # break
# used (88, 113, -1104) (168, -1125, 72)
# used (68, -1246, -43)
# [-1037, 41, -1272]