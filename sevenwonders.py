#Jacob Pawlak
#February 14th, 2017 Happy Valentines Day
#Seven Wonders
#https://open.kattis.com/problems/sevenwonders

from math import *
def main():

	cards = input()
	tablet = 0
	compass = 0
	gear = 0
	points = 0
	bonus_pts = 0;
	for i in range(0, len(cards)):
		if(cards[i] == "T"):
			tablet += 1
		if(cards[i] == "C"):
			compass += 1
		if(cards[i] == "G"):
			gear += 1

	TCG = [tablet, compass, gear]
	bonus_pts = min(TCG)	
	if(compass > 0):
		points += pow(compass, 2)
	if(tablet > 0):
		points += pow(tablet, 2)
	if(gear > 0):
		points += pow(gear, 2)
	points += bonus_pts * 7
	print(int(points))
main()
