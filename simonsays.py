#Jacob Pawlak
#November 13th 2017
#Simon Says
#https://open.kattis.com/problems/simonsays

def main():

	num_phrases = int(input())
	for i in range(0, num_phrases):
		phrase = input()
		if(phrase[:10] == "Simon says"):
			print(phrase[11:])

main()
