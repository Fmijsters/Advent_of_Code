import numpy as np

def match(image_to_match,v):
	top_to_match = np.asarray(image_to_match[0])
	bottom_to_match = np.asarray(image_to_match[-1])
	left_to_match = np.asarray(image_to_match[:,0])
	right_to_match = np.asarray(image_to_match[:,-1])
	top = np.asarray(v[0])
	bottom = np.asarray(v[-1])
	left = np.asarray(v[:,0])
	right = np.asarray(v[:,-1])
	if (top == top_to_match).all():
		print(k)
	if (bottom == bottom_to_match).all():
		print(k)
	if (left == left_to_match).all():
		print(k)
	if (right == right_to_match).all():
		print(k)

with open('input.txt') as f:
	camera_array = f.read().split('\n\n')
	# print(camera_array)
	cleaned_camera_array = {}
	for camera_image in camera_array:
		# print(camera_image)
		splitted = [line for line in camera_image.split('\n')]
		# print(splitted)
		
		cleaned_camera_array[int(splitted[0][5:-1])] = np.asarray([list(row) for row in splitted[1:]])
		# break
	# print(cleaned_camera_array)
	image_to_match = cleaned_camera_array[2311]
	
	for k,v in cleaned_camera_array.items():
		if k == 2311:
			continue
		# print(k)
		# print(v)
		match(image_to_match,v)
		v=v.T
		match(image_to_match,v)
		v=v.T
		match(image_to_match,v)
		v=v.T
		match(image_to_match,v)
		v=v.T
		match(image_to_match,v)