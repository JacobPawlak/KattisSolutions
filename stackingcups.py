#Jacob Pawlak
#February 13th, 2017
#Stacking Cups
#https://open.kattis.com/problems/cups

def by_size_key(color):
	return color[1];

def main():

	digits = ['0','1','2','3','4','5','6','7','8','9']
	times = int(input())
	color_list = []
	for i in range(0, times):
		new_color = input()
		new_pair = new_color.split()
		if(new_pair[0][0:1] in digits):
			reversed_pair = [new_pair[1], (int(new_pair[0]) / 2)]
			color_list.append(reversed_pair)
		else:
			new_pair[1] = int(new_pair[1])
			color_list.append(new_pair)
	#print(color_list)
	sorted_colors = sorted(color_list, key = by_size_key)
	#print(sorted_colors)
	for color in sorted_colors:
		print(color[0])

main()
