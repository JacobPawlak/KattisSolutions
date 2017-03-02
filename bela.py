#Jacob Pawlak
#March 2nd 2017
#Bela
#https://open.kattis.com/problems/bela

def main():

	hands_suit = input()
	hands_suit = hands_suit.split()
	hands = int(hands_suit[0]) * 4
	suit = hands_suit[1]
	score = 0
	for i in range(0, hands):
		card = input()
		ctype = card[0]
		csuit = card[1]
		if(ctype == "A"):
			score += 11
			if(suit == csuit):
				score += 0
		if(ctype == "K"):
			score += 4
			if(suit == csuit):
				score == 0
		if(ctype == "Q"):
			score += 3
			if(suit == csuit):
				score += 0
		if(ctype == "J"):
			score += 2
			if(suit == csuit):
				score += 18
		if(ctype == "T"):
			score += 10
			if(suit == csuit):
				score += 0
		if(ctype == "9"):
			score += 0
			if(suit == csuit):
				score += 14
		if(ctype == "8"):
			score += 0
			if(suit == csuit):
				score += 0
		if(ctype == "7"):
			score += 0
			if(suit == csuit):
				score += 0
	print(score)
main()
