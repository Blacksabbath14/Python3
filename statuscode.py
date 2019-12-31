#!/bin/python3

import sys #importing sys module

def main():
	if (len(sys.argv)>=3): 
		print('You have entered the correct number of arguments')
	else:
		print('Invalid number of arguments')
		#exit(20)
		sys.exit(20) #status code  
		
if __name__=='__main__':    #basic definition
	main()