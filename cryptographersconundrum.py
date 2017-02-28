#Jacob Pawlak
#February 28th, 2017
#Cryptographer's Conundrum
#https://open.kattis.com/problems/conundrum

def main():

	puzzle = input()
	num_swaps = 0
	for i in range(0, len(puzzle)):
		if(i % 3 == 0):
			if(puzzle[i] != "P"):
				num_swaps += 1
		if(i % 3 == 1):
			if(puzzle[i] != "E"):
				num_swaps += 1
		if(i % 3 == 2):
			if(puzzle[i] != "R"):
				num_swaps += 1
	print(num_swaps)

main()
