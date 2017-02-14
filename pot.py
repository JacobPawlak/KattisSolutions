#Jacob Pawlak
#February 14th, 2017 Happy Valentines day
#Pot
#https://open.kattis.com/problems/pot

from math import *

def main():

	nums = int(input())
	sums = 0
	for i in range(0, nums):
		wrong_num = input()
		base = int(wrong_num[:-1])
		power = int(wrong_num[len(wrong_num) -1:])
		sums += pow(base, power)

	print(int(sums))
main()
