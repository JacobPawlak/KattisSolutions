//Jacob Pawlak
//February 14th, 2017 Happy Valentines day!
//Pot
//https://open.kattis.com/problems/pot

#include<iostream>
#include<cmath>
#include<string>

using namespace std;

int main(){

	int nums = 0;
	cin >> nums;
	long sums = 0;
	for(int i = 0; i < nums; i++){

		string wrong_num = "";
		cin >> wrong_num;
		int base = 0;
		int power = 0;
		base = stoi(wrong_num.substr(0, wrong_num.length() -1));
		power = stoi(wrong_num.substr(wrong_num.length() - 1, wrong_num.length()));

		sums += pow(base, power);
	}
	cout << sums << endl;

	return 0;
}
