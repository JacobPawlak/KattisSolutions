#Jacob Pawlak
#February 23rd, 2017
#Kemija
#https://open.kattis.com/problems/kemija08

import string

def main():

	coded = input()
	coded = coded.replace("apa", "a")
	coded = coded.replace("epe", "e")
	coded = coded.replace("ipi", "i")
	coded = coded.replace("opo", "o")
	coded = coded.replace("upu", "u")
	print(coded)

main()
