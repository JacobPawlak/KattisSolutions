#Jacob Pawlak
#November 13th, 2017
#Un-bear-able Zoo
#https://open.kattis.com/problems/zoo


def main():

	num_descrip = int(input())
	list_num = 1
	while(num_descrip > 0):
		animals= {}
		for i in range(0, num_descrip):
			animal = input()
			animal = animal.split()
			animal = animal[len(animal) - 1].lower()
			#print(animal)
			if(animal in animals.keys()):
				animals[animal] += 1
				#print(animals[animal])
			else:
				animals.update({animal:1})
			#print(animals)
		print("List " + str(list_num) + ":")
		for ani in sorted(animals.keys()):
			print(ani + " | " + str(animals[ani]))
		list_num += 1
		num_descrip = int(input())
main()
