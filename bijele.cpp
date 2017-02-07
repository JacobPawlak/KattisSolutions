//Jacob Pawlak
//February 6 2017
//Bijele
//https://open.kattis.com/problems/bijele

#include<iostream>
#include<array>

using namespace std;

int main(){

	int pieces[6] = {1,1,2,2,2,8};
	for(int i = 0; i < 6; i++){
		int mirko = 0;
		cin >> mirko;
		cout << (pieces[i] - mirko) << " ";
	}
	cout << endl;

	return 0;
}
