#Jacob Pawlak
#February 6 2017
#Bijele
#https://open.kattis.com/problems/bijele

def main():

	pieces = [1,1,2,2,2,8]
	str = input()
	sstr = str.split()
	for i in range(0, 6):
		print(pieces[i] - int(sstr[i]), end=" ")
	print()
main()
