#Jacob Pawlak
#February 15th, 2017
#Ladder
#https://open.kattis.com/problems/ladder

from math import *

def main():

	building = input()
	building_list = building.split()
	height = int(building_list[0])
	degrees = int(building_list[1])
	rads = radians(degrees)
	ladder = int(ceil(height / sin(rads)))
	print(ladder)

main()
