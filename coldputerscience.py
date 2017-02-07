#Jacob Pawlak
#February 6 2017
#Cold-puter Science
#https://open.kattis.com/problems/cold

def main():

	times = int(input())
	str = input()
	sstr = str.split()
	coldDays = 0
	for i in range(0, times):
		if(int(sstr[i]) < 0):
			coldDays += 1
	print(coldDays)
main()
