#!/bin/python3
import sys
import binascii

def strip(to_strip):
	fin=str(to_strip)
	print(fin[2:-1])
	#print(type(to_strip))
	

def bin_to_ascii(bin):
	asc = int(bin,2)
	print(binascii.unhexlify('%x' % asc))
	asc_fin=binascii.unhexlify('%x' % asc)
	print(asc_fin)
	strip(asc_fin)

def decode(file):
	f1 = open(file,'r')
	file_o = f1.readline()
	f1.close()
	flag=[]
	for pr in file_o:
		if ( pr ==' ' ):
			flag.append('1')
		else:
			flag.append('0')	
	flag = list(map(int, flag))
	#print(len(flag))
	format(flag)

def format(bin):
	fin = ''
	for i in bin:
		fin=fin + str(bin[i])
	print(fin,' And length of the string is ', len(fin))
	bin_to_ascii(fin)

def main():
	decode(sys.argv[1])


if __name__ == '__main__' :
	main()