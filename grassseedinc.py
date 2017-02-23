#Jacob Pawlak
#February 23rd, 2017
#Grass Seed Inc
#https://open.kattis.com/problems/grassseed

def main():

	price = float(input())
	num_lawns = int(input())
	total_cost = 0
	for i in range(0, num_lawns):
		lawn = input()
		lawn = lawn.split()
		width = float(lawn[0])
		length = float(lawn[1])
		total_cost += (price*width*length)
	print('{0:.10}'.format(total_cost))

main()
