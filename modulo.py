#Jacob Pawlak
#February 15th 2017
#Modulo
#https://open.kattis.com/problems/modulo

def main():

	dif_mods = []
	for i in range(0, 10):
		num = int(input())
		mod = num % 42
		if(mod not in dif_mods):
			dif_mods.append(mod)

	print(len(dif_mods))


main()
