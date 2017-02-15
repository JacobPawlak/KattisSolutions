//Jacob Pawlak
//February 15th, 2017
//Ladder
//https://open.kattis.com/problems/ladder

#include<iostream>
#include<cmath>

using namespace std;

int main(){

	int height, degrees = 0;
	cin >> height >> degrees;
	int ladder = 0;
	float pi = 3.14159;
	float radians = (degrees * pi / 180);
	ladder = height / sin(radians);
	ladder++;

	cout << ladder << endl;

	return 0;
}
