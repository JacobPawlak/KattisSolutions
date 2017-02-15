//Jacob Pawlak
//February 15th, 2017
//Oddities
//https://open.kattis.com/problems/pet

#include<iostream>

using namespace std;

int main(){

	int times = 0;
	cin >> times;
	for(int i = 0; i < times; i++){

		int num = 0;
		cin >> num;
		if(num % 2 == 0)
			cout << num << " is even" << endl;
		else
			cout << num << " is odd" << endl;
	}

	return 0;
}
