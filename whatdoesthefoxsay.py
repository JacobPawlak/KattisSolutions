#Jacob Pawlak
#January 13th, 2018
#What does the fox say
#https://open.kattis.com/problems/whatdoesthefoxsay

def main():

	num_tests = int(input())

	for i in range(0, num_tests):
		animals = {}
		record = input()
		r_split = record.split()
		info = input()
		while(info != "what does the fox say?"):
			info = info.split()
			animals[info[0]] = info[2]
			info = input()
		for animal in animals.keys():
			if(animals[animal] in r_split):
				for j in range(0, r_split.count(animals[animal])):
					r_split.remove(animals[animal])

		res = ""
		for sound in r_split:
			res = res + sound + " "
		res = res[:-1]
		print(res)
main()

