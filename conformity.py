#Jacob Pawlak
#January 18th, 2018
#Conformity
#https://open.kattis.com/problems/conformity


def main():

	frosh = int(input())
	f_classes = {}
	for i in range(0, frosh):
		classes = input()
		classes = classes.split()
		new_classes = []
		for clas in classes:
			new_classes.append(int(clas))
		sort_classes = sorted(new_classes)
		key = ""
		for clas in sort_classes:
			key += str(clas) + " "
		if key not in f_classes.keys():
			f_classes[key] = 1
		else:
			f_classes[key] += 1
	seen_top = 0
	top = 0
	for sched in f_classes.keys():
		if f_classes[sched] > top:
			top = f_classes[sched]
			seen_top = 1
		elif f_classes[sched] == top:
			seen_top += 1
	print(seen_top * top)

main()
