#Jacob Pawlak
#November 13th, 2017
#Left Beehind
#https://open.kattis.com/problems/leftbeehind


def main():

	honeys = input()
	honeys = honeys.split()
	sweet = int(honeys[0])
	sour = int(honeys[1])
	while( (sweet > 0) or (sour > 0) ):
		if( (sweet + sour) == 13):
			print("Never speak again.")
		elif( sweet < sour ):
			print("Left beehind.")
		elif( sweet > sour ):
			print("To the convention.")
		else:
			print("Undecided.")
		honeys = input()
		honeys = honeys.split()
		sweet = int(honeys[0])
		sour = int(honeys[1])

main()
