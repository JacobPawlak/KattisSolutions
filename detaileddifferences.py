#Jacob Pawlak
#February 23rd, 2017
#Detailed Differences
#https://open.kattis.com/problems/detaileddifferences

def main():

	num_times = int(input())
	for i in range(0, num_times):
		first = input()
		second = input()
		diff = ""
		for j in range(0, len(first)):
			if(first[j] == second[j]):
				diff += "."
			else:
				diff += "*"
		print(first)
		print(second)
		print(diff)
		print()

main()
