#Jacob Pawlak
#February 14th 2017 Happy Valentines Day
#Spavanac
#https://open.kattis.com/problems/spavanac

def main():

	time_str = input()
	time_list = time_str.split()
	hours = int(time_list[0])
	mins = int(time_list[1])
	mins = mins - 45
	if(mins < 0):
		mins += 60
		hours -= 1
		if(hours < 0):
			hours = 23
	print(hours, mins)


main()
