import os
import binascii

def get_subnet():
	os.system('ifconfig | grep netmask > subnet.txt') 
	with open('subnet.txt') as f:
		fields = f.readlines()[-1].rstrip().split()
		binary_num = bin(int(fields[3][2:],16))[2:]
		num_ones = binary_num.find('0')
		my_ip = fields[1].split('.')
		my_ip = list(map(int,my_ip))
		mask_dec = list()
		for i in range(0,25,8):
			mask_dec.append(int(binary_num[i:i+8],2))
		my_router = list()
		for i in range(0,4):
			my_router.append(str(mask_dec[i] & my_ip[i]))
		return (".".join(my_router)+'/'+str(num_ones))