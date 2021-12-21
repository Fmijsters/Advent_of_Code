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


with open('input.txt') as f:
	hex_input = f.read().rstrip()
	input_binary = decode_hex(hex_input)
	print(input_binary)
	index=0
	versions=[]
	while index < len(input_binary) and not len(set(input_binary[index:]))==1:
		version = int(input_binary[index:index+3],2)
		index+=3
		versions.append(version)
		type_id = int(input_binary[index:index+3],2)
		index+=3
		print('version',version,'type_id',type_id)
		if type_id == 4:
			print("decoding literal value")
			literal_value = decode_literal_value(input_binary[index:])
			index += int(len(literal_value) + len(literal_value)/4)
		else:
			length_type_id = input_binary[index]
			print('length_type_id',length_type_id)
			index+=1
			if length_type_id == "0":
				length_subset = input_binary[index:index+15]
				print("decoding operator length",int(length_subset,2))
				index += 15

			elif length_type_id == "1":
				num_subset = input_binary[index:index+11]
				print("decoding operator number",int(num_subset,2))
				index += 11
	print(sum(versions))