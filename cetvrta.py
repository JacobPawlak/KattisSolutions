#Jacob Pawlak
#February 28th, 2017
#Cetvrta
#https://open.kattis.com/problems/cetvrta

def main():

	point1 = input()
	point2 = input()
	point3 = input()
	point1 = point1.split()
	point2 = point2.split()
	point3 = point3.split()

	xs = []
	ys = []
	if(int(point1[0]) not in xs):
		xs.append(int(point1[0]))
	if(int(point2[0]) not in xs):
		xs.append(int(point2[0]))
	if(int(point3[0]) not in xs):
		xs.append(int(point3[0]))
	if(int(point1[1]) not in ys):
		ys.append(int(point1[1]))
	if(int(point2[1]) not in ys):
		ys.append(int(point2[1]))
	if(int(point3[1]) not in ys):
		ys.append(int(point3[1]))

	given = [point1, point2, point3]
	#print(given)
	all = [[str(xs[0]),str(ys[0])],[str(xs[0]),str(ys[1])],[str(xs[1]),str(ys[0])],[str(xs[1]),str(ys[1])]]
	#print(all)
	for i in range(0,4):
		if(all[i] not in given):
			found = all[i]
			print(found[0], found[1])


main()
