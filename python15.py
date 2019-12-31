#!/bin/python3
import sys
import collections
def main():

	try:
		file_obj=open(sys.argv[1],'r')
		a=file_obj.read().split()
		a=[x.lower() for x in a]
		a.sort()
		list=[]
		for i in range(len(a)):
			b=a[i]
			list.append(b)
		final=collections.Counter(list)
		keys=final.keys()
		for k in keys:
			print(k,final[k])

	except IndexError:
		print('Please Enter The File Name')
	except KeyboardError:
		print('Nope Try Again')

	finally:
		pass
if __name__=='__main__':
	main()
