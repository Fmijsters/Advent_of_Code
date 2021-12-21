import numpy as np
import matplotlib.pyplot as plt

def find_path(current_path,destination,grid,visited,x,y,all_paths):
	max_val = len(grid)
	distmap=np.ones((max_val,max_val),dtype=int)*np.Infinity
	distmap[0,0]=0
	originmap=np.ones((max_val,max_val),dtype=int)*np.nan
	visited=np.zeros((max_val,max_val),dtype=bool)
	finished = False
	x,y=np.int(0),np.int(0)
	count=0
	#Loop Dijkstra until reaching the target cell
	while not finished:
	  # move to x+1,y
	  if x < max_val-1:
	    if distmap[x+1,y]>grid[x+1,y]+distmap[x,y] and not visited[x+1,y]:
	      distmap[x+1,y]=grid[x+1,y]+distmap[x,y]
	      originmap[x+1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
	  # move to x-1,y
	  if x>0:
	    if distmap[x-1,y]>grid[x-1,y]+distmap[x,y] and not visited[x-1,y]:
	      distmap[x-1,y]=grid[x-1,y]+distmap[x,y]
	      originmap[x-1,y]=np.ravel_multi_index([x,y], (max_val,max_val))
	  # move to x,y+1
	  if y < max_val-1:
	    if distmap[x,y+1]>grid[x,y+1]+distmap[x,y] and not visited[x,y+1]:
	      distmap[x,y+1]=grid[x,y+1]+distmap[x,y]
	      originmap[x,y+1]=np.ravel_multi_index([x,y], (max_val,max_val))
	  # move to x,y-1
	  if y>0:
	    if distmap[x,y-1]>grid[x,y-1]+distmap[x,y] and not visited[x,y-1]:
	      distmap[x,y-1]=grid[x,y-1]+distmap[x,y]
	      originmap[x,y-1]=np.ravel_multi_index([x,y], (max_val,max_val))

	  visited[x,y]=True
	  dismaptemp=distmap
	  dismaptemp[np.where(visited)]=np.Infinity
	  # now we find the shortest path so far
	  minpost=np.unravel_index(np.argmin(dismaptemp),np.shape(dismaptemp))
	  x,y=minpost[0],minpost[1]
	  if x==max_val-1 and y==max_val-1:
	    finished=True
	  count=count+1

	mattemp=grid.astype(float)
	x,y=max_val-1,max_val-1
	path=[]
	mattemp[np.int(x),np.int(y)]=np.nan

	while x>0.0 or y>0.0:
	  path.append([np.int(x),np.int(y)])
	  xxyy=np.unravel_index(np.int(originmap[np.int(x),np.int(y)]), (max_val,max_val))
	  x,y=xxyy[0],xxyy[1]
	  mattemp[np.int(x),np.int(y)]=np.nan
	path.append([np.int(x),np.int(y)])

	print('The path length is: '+np.str(distmap[max_val-1,max_val-1]))





with open('input.txt') as f:
	grid = [[int(number) for number in line.rstrip()] for line in f.readlines()]
	# print(grid)
	gri = []
	# for i in range(5):
		# gri.append([[],[],[],[],[]])
	# print(gri)
	whole_grid = np.zeros((len(grid)*5,len(grid[0]*5)))
	# print(whole_grid)
	# for row_i,row in enumerate(whole_grid):
		# for col_i,col in enumerate(row):

	for i in range(5):
		for j in range(5):
			# print(i,j)
			for k in range(len(grid)):
				for l in range(len(grid[0])):
					# print(i,j,k,l)
					whole_grid[i*len(grid) + k][j*len(grid[0])+l] = grid[k][l] + i+j
					if whole_grid[i*len(grid) + k][j*len(grid[0])+l] > 9:
						whole_grid[i*len(grid) + k][j*len(grid[0])+l] = whole_grid[i*len(grid) + k][j*len(grid[0])+l]-9
	# for r in whole_grid:
		# print(r)

			
	



	# exit(1)
	grid = whole_grid
	starting_position = [0,0]
	destination = [len(grid)-1,len(grid[0])-1]
	print(starting_position,destination)
	find_path([starting_position],destination,np.asarray(grid),[starting_position],0,0,[])
