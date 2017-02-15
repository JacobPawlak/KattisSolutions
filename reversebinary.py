#Jacob Pawlak
#February 15th, 2017
#Reverse Binary
#https://open.kattis.com/problems/reversebinary

def rev_str(str):

	rev_str = ""
	for i in range(0, len(str)):
		rev_str += str[(len(str) - 1 - i)]

	return rev_str

def main():

	decimal_num = int(input())
	binary_str = (bin(decimal_num))[2:]
	rev_binary = rev_str(binary_str)
	new_decimal = int(rev_binary, 2)
	print(new_decimal)
		
main()
