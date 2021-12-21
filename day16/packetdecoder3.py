def decode_hex(hex_input):
	decode_map = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
	return ''.join([decode_map[inp] for inp in list(hex_input)])

def decode_literal_value(input_binary):
	literal_value=""
	index=0
	part = input_binary[:5]
	while True:
		literal_value+=part[1:]
		index+=5
		if part[0] == '0':
			break
		part = input_binary[index:index+5]
	return literal_value	


def decode_binary(input_binary,values):
	index = 0
	version = int(input_binary[:3],2)
	index+=3
	input_binary=input_binary[3:]
	versions.append(version)
	type_id = int(input_binary[:3],2)
	index+=3
	input_binary=input_binary[3:]
	if type_id == 4:
		literal_value = decode_literal_value(input_binary)
		index += int(len(literal_value) + len(literal_value)/4)
		input_binary = input_binary[int(len(literal_value) + len(literal_value)/4):]
		return index, input_binary, int(literal_value,2)
	else:
		length_type_id = input_binary[0]
		index+=1
		input_binary=input_binary[1:]
		if length_type_id == "0":
			length_subset = int(input_binary[:15],2)
			index += 15
			input_binary = input_binary[15:]
			child_index = 0
			values= []
			while child_index != length_subset:
				child_index_read, input_binary, value = decode_binary(input_binary,values)
				values.append(value)
				child_index+=child_index_read
			index += child_index
		elif length_type_id == "1":
			num_subset = int(input_binary[:11],2)
			input_binary = input_binary[11:]
			index += 11
			child_index,read_subsets = 0,0
			values= []
			while num_subset != read_subsets:
				child_index_read, input_binary,value = decode_binary(input_binary,values)
				child_index += child_index_read
				read_subsets+=1
				values.append(value)
			index += child_index
		value = 0
		if type_id == 0:
			value = sum(values)
		elif type_id == 1:
			value= 1
			for val in values:
				value *= val
		elif type_id == 2:
			value = min(values)
		elif type_id == 3:
			value = max(values)
		elif type_id == 5:
			if values[0] > values[1]:
				value = 1
		elif type_id == 6:
			if values[0] < values[1]:
				value = 1
		elif type_id == 7:
			if values[0] == values[1]:
				value = 1
		return index, input_binary,value


with open('input.txt') as f:
	hex_input = f.read().rstrip()
	input_binary = decode_hex(hex_input)
	versions=[]
	i,r,value = decode_binary(input_binary,versions)	
	print(value)