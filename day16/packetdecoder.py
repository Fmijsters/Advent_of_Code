def decode_literal_value(binary_input):
	version = int(binary_input[:3],2)
	type_id = int(binary_input[3:6],2)
	literal_value = ''
	# print('version',version)
	# print('type_id',type_id)
	# print()
	for i in range(len(binary_input[6:])//5):
		part = binary_input[6+i*5:6+i*5+5]
		group_classifier = part[0]
		if group_classifier != 0:
			literal_value+=part[1:]
	value = int(literal_value,2)
	return version,type_id,value

def decode_hex(hex_input):
	decode_map = {"0":"0000","1":"0001","2":"0010","3":"0011","4":"0100","5":"0101","6":"0110","7":"0111","8":"1000","9":"1001","A":"1010","B":"1011","C":"1100","D":"1101","E":"1110","F":"1111"}
	return ''.join([decode_map[inp] for inp in list(hex_input)])

def decode_sub_packets_by_length(binary_input,length):
	# print(binary_input)
	sub_packets = []
	starting_index = 0
	end_index = 0
	# print(binary_input,length,len(binary_input))
	counter = 0
	while end_index < length:
		# print(sub_packet_type,end_index)\
		# print(sub_packets)
		sub_packet_type = int(binary_input[starting_index+3:starting_index+6],2) 

		# print(binary_input[starting_index:])
		# print()
		# print(sub_packet_type,binary_input[starting_index+3:starting_index+6])
		if sub_packet_type == 4:
			length_subpack = find_length_literal_subpacket(binary_input[starting_index:])
			end_index = starting_index+length_subpack
			sub_packets.append(binary_input[starting_index:end_index])
			# print()		
			# print(binary_input[starting_index:end_index])
			# print()		
			starting_index = end_index
		else:
			identifier_type = binary_input[starting_index+6]
			if identifier_type == '0':
				length_subpack = int(binary_input[starting_index+6+1:starting_index+6+1+15],2)
				# print('length',length_subpack)
				end_index = starting_index+6+1+15+length_subpack
				sub_packets.append(binary_input[starting_index:end_index])
				# print()
				# print(binary_input[starting_index:end_index])
				# print()

				# print(binary_input[starting_index:end_index])
				# print(starting_index,end_index)
				starting_index = end_index
				# print(end_index)
			# 	break
			else:
				amount = int(binary_input[starting_index+7:starting_index+7+11],2)
				# print('idt',identifier_type,amount)
				# print(binary_input[starting_index+7+11:])
				# print(identifier_type,amount)
				# print(binary_input[starting_index:])
				inter_subpacks = decode_sub_packets_by_number(binary_input[starting_index+7+11:],amount)
				# print(inter_subpacks)
				length_subpack = len(''.join(inter_subpacks))
				# print(length_subpack)
				end_index = starting_index+6+1+11+length_subpack
				# print(starting_index,end_index)
				# print()
				# print(binary_input[starting_index:end_index])
				# print()

				sub_packets.append(binary_input[starting_index:end_index])
				# print(binary_input[starting_index:end_index])

				starting_index = end_index

		counter+=1
		# print('eid',end_index)
		# if counter == 4:
			# print(sub_packets)
			# exit(0)
		# break
	return sub_packets

def find_length_literal_subpacket(binary_input):

	version = int(binary_input[:3],2)
	type_id = int(binary_input[3:6],2)
	# print(version,type_id)

	# print(binary_input[6:])

	for i in range(len(binary_input[6:])//5):
		part = binary_input[6+i*5:6+i*5+5]
		# print(part)
		group_classifier = part[0]
		if group_classifier != '0':
			pass
			# print(part)
			# literal_value+=part[1:]
		elif group_classifier == '0':
			# print(part)
			#end index
			return 6+i*5+5
			break
	return -1

#  4   2  11      1       1   2  11      1       5   2  15         4
# 100 010 1 00000000001 001 010 1  00000000001 101 010 0 000000000001011 110 100 01111 000
#  3   0  11      2      0   0  11     2        6
# 011 000 1 00000000010 000 000 0 000000000010 110 000 10001 01010 110 001 01100 10001 00000 000010000100011000111000110100
def decode_sub_packets_by_number(binary_input,amount):
	# print(binary_input)
	sub_packets = []
	starting_index = 0
	end_index = 0
	if amount ==1:
		sub_packets.append(binary_input)
	else:
		# print('here',binary_input)
		while len(sub_packets) != amount:
			index = 0 
			sub_packet_type = int(binary_input[starting_index+3:starting_index+6],2) 
			# print(sub_packet_type)
			# print(sub_packet_type)
			if sub_packet_type== 4:
				length_subpack = find_length_literal_subpacket(binary_input[starting_index:])
				# print(length_subpack)
				end_index = starting_index+length_subpack
				# print(starting_index,end_index)
				# print(len(binary_input[starting_index:end_index]))
				sub_packets.append(binary_input[starting_index:end_index])
				starting_index = end_index
			else:
				identifier_type = binary_input[starting_index+6]
				# print(identifier_type)
				if identifier_type == '0':
					length_subpack = int(binary_input[starting_index+6+1:starting_index+6+1+15],2)
					# print(binary_input[starting_index+6+1:starting_index+6+1+15],length_subpack)
					end_index = starting_index+6+1+15+length_subpack
					sub_packets.append(binary_input[starting_index:end_index])
					starting_index = end_index
				else:
					amount = int(binary_input[starting_index+7:starting_index+7+11],2)
					inter_subpacks = decode_sub_packets_by_number(binary_input[starting_index+7+11:],amount)
					length_subpack = len(''.join(inter_subpacks))
					end_index = starting_index+6+1+15+length_subpack
					sub_packets.append(binary_input[starting_index:end_index])


					# break
				# break
	# print(sub_packets)
	return sub_packets


#  3   0  11     2
# 011 000 1 00000000010 
#  0   0  15      22			 4			   4
# 000 000 0 000000000010110 000 100 01010 101 100 01011         
#  1   0  11      2			 4             4
# 001 000 1 00000000010 000 100 01100 011 100 01101 00


# represents an operator packet (version 3) which contains two sub-packets; each sub-packet is an operator packet that contains two literal values. This packet has a version sum of 12.
def decode_operator(binary_input,versions):
	version = int(binary_input[:3],2)
	type_id = int(binary_input[3:6],2)
	length_type_id = int(binary_input[6],2)
	# print('version',version)
	# print('type_id',type_id)
	# print('length_type_id',length_type_id)
	# print()
	sub_packets = []
	if length_type_id == 0:
		length_sub_packets = int(binary_input[7:7+15],2)
		# print(length_sub_packets)
		sub_packets = decode_sub_packets_by_length(binary_input[22:22+length_sub_packets],length_sub_packets)
		# sub_packets.append(binary_input[22:22+length_sub_packets])
	elif length_type_id == 1:
		number_sub_packets = int(binary_input[7:7+11],2)
		# print('number of sub packets',number_sub_packets)
		sub_packets = decode_sub_packets_by_number(binary_input[18:],number_sub_packets)
		# print(sub_packets)
		# print(sub_packets)
	for sub_packet in sub_packets:
		# print('sub_packet',int(sub_packet[3:6],2))

		# print()
		if int(sub_packet[3:6],2) != 4:
			v,t,s,_= decode_operator(sub_packet,versions)
			versions.append(v)
		else: 
			v,t,v1 = decode_literal_value(sub_packet)
			versions.append(v)

	return version,type_id,sub_packets,versions



with open('input.txt') as f:
	
	# print(hex_input)
	# hex_input = "D2FE28"
	# decoded_input = decode_hex(hex_input)
	# version,type_id,value = decode_literal_value(decoded_input)

	# hex_input = "38006F45291200"
	# decoded_input = decode_hex(hex_input)
	# version,type_id,sub_packet_decoded_list = decode_operator(decoded_input)

	# hex_input = "EE00D40C823060"
	# decoded_input = decode_hex(hex_input)
	# versions=[]
	# version,type_id,sub_packet_decoded_list,versions = decode_operator(decoded_input,versions)
	# versions.append(version)
	# print(versions)
	# print(sum(versions))

	# print(versions)
	hex_input = "8A004A801A8002F478"
	decoded_input = decode_hex(hex_input)
	versions= []
	version,tid,sub_packets,versions = decode_operator(decoded_input,versions)
	versions.append(version)
	print(sum(versions))

#  3   0  11     2
# 011 000 1 00000000010 
#  0   0  15      22			 4			   4
# 000 000 0 000000000010110 000 100 01010 101 100 01011         
#  1   0  11      2			 4             4
# 001 000 1 00000000010 000 100 01100 011 100 01101 00
	hex_input = "620080001611562C8802118E34"
	decoded_input = decode_hex(hex_input)
	# print(decoded_input)
	versions= []
	version,tid,sub_packets,versions = decode_operator(decoded_input,versions)
	print(sub_packets)
	versions.append(version)
	print(sum(versions))

#  3   0  15        84
# 110 000 0 000000001010100 
#  0   0  15        22        0   4         6   4  
# 000 000 0 000000000010110 000 100 01010 110 100 01011 
#  4   0  11     2       7   4         0   4 
# 100 000 1 00000000010 111 100 01100 000 100 01101 000000
	hex_input = "C0015000016115A2E0802F182340"
	decoded_input = decode_hex(hex_input)
	# print(decoded_input)
	versions= []
	version,tid,sub_packets,versions = decode_operator(decoded_input,versions)
	versions.append(version)
	# print(versions)
	print(sum(versions))

	hex_input = "A0016C880162017C3686B18A3D4780"
	decoded_input = decode_hex(hex_input)
	# print(decoded_input)
	versions= []
	version,tid,sub_packets,versions = decode_operator(decoded_input,versions)
	versions.append(version)
	# print(versions)
	print(sum(versions))

	# hex_input = f.read().rstrip()
	# # print(len("010100100111000100000100100101111001011011111011100010000111001010100000110100100101101110011111101101110100011010001001001110000100011100100011"))
	# decoded_input = decode_hex(hex_input)
	# print(decoded_input)
	# versions= []
	# version,tid,sub_packets,versions = decode_operator(decoded_input,versions)
	# versions.append(version)
	# # print(versions)
	# print(sum(versions))