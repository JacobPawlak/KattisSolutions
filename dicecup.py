#Jacob Pawlak
#February 6 2017
#DiceCup
#https://open.kattis.com/problems/dicecup

def main():

	str = input()
	strs = str.split()
	d1 = int(strs[0])
	d2 = int(strs[1])
	bigger = d1
	smaller = d2
	if(d1 < d2):
		bigger = d2
		smaller = d1
	for i in range(smaller, bigger + 1):
		print(i + 1)

main()
