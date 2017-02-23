#Jacob Pawlak
#February 23rd, 2017
#I've Been Everywhere Man
#https://open.kattis.com/problems/everywhere

def main():

	num_times = int(input())
	city_list = []
	for i in range(0, num_times):
		num_cities = int(input())
		for j in range(0, num_cities):
			city = input()
			if (city not in city_list):
				city_list.append(city)
		print(len(city_list))
		city_list = []

main()
