with open('input.txt') as f:
	target_area = f.read().rstrip()
	print(target_area)
	target_area= target_area.replace('target area: x=','').replace(', y=',' ')
	x,y = target_area.split(' ')
	x1,x2 = [int(hor) for hor in x.split('..')]
	y1,y2 = [int(ver) for ver in y.split('..')]
	best_coords = [0,0]
	highest_coord= 0
	positions=[]
	with open('velocities.txt') as g:
		velocities = [[int(coord) for coord in line.rstrip().split(',')] for line in g.readlines()]
	for yi in range(y1-1,1000):
		for xi in range(0,x2+1):
			ys= []
			velocity=[xi,yi]
			probe = [0,0]
			initial_velocity=velocity.copy()
			while True:
				probe = [coord + velocity[i] for i,coord in enumerate(probe)]
				if velocity[0] > 0: velocity[0]-=1
				elif velocity[0] < 0: velocity[0]+=1
				velocity[1] -=1
				ys.append(probe[1])
				if x1<= probe[0] <=x2 and y1 <= probe[1]  <= y2:
					if max(ys)>highest_coord:
						highest_coord = max(ys)
					positions.append(initial_velocity)

					break
				if probe[1] < y1 or probe[0] > x2:
					break
	print(len(positions))
