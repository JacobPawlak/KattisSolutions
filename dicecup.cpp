//Jacob Pawlak
//February 6 2017
//DiceCup
//https://open.kattis.com/problems/dicecup

#include<iostream>

using namespace std;

int main(){

	int d1, d2;

	cin >> d1 >> d2;

	int bigger = d1;
	int smaller = d2;
	if(d2 > d1){
		bigger = d2;
		smaller = d1;
	}
	for(int i = smaller; i <= bigger; i++){
		cout << i + 1 << endl;
	}

	return 0;
}
