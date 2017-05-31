#Jacob Pawlak
#May 30th, 2017
#A Real Challenge
#https://open.kattis.com/problems/areal

from math import *

def main():

	#get the input (it will be a square area of a pasture)
	pasture = float(input())
	root_of_pasture = pow(pasture, .5)
	#the total length of the fence is 4 * the side length ^^
	print(4 * root_of_pasture)


main()
