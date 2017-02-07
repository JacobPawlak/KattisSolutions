#Jacob Pawlak
#February 6 2017
#FizzBuzz
#https://open.kattis.com/problems/fizzbuzz

def main():

	str = input()
	arr = str.split()
	x = int(arr[0])
	y = int(arr[1])
	n = int(arr[2])
	for i in range(1, n + 1):
		if((i % x == 0) and (i % y == 0)):
			print("FizzBuzz")
		elif(i % x == 0):
			print("Fizz")
		elif(i % y == 0):
			print("Buzz")
		else:
			print(i)
main()
