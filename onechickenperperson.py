#Jacob Pawlak
#May 30th, 2017
#One Chicken Per Person
#https://open.kattis.com/problems/onechicken

def main():

	#get n and m (note: n != m)
	nm = input()
	nm = nm.split()
	#set n and m
	n = int(nm[0])
	m = int(nm[1])
	dif = m - n
	if(dif == 1):
		print("Dr. Chaz will have 1 piece of chicken left over!")
	elif(dif > 1):
		print("Dr. Chaz will have", dif, "pieces of chicken left over!")
	elif(dif == -1):
		print("Dr. Chaz needs 1 more piece of chicken!")
	else:
		print("Dr. Chaz needs", (0 - dif), "more pieces of chicken!")


main()
