//Jacob Pawlak
//February 6 2017
//Cold-puter Science
//https://open.kattis.com/problems/cold

#include<iostream>

using namespace std;

int main(){

	int times = 0;
	int coldDays = 0;
	cin >> times;
	for(int i = 0; i < times; i++){
		int newTemp = 0;
		cin >> newTemp;
		if(newTemp < 0)
			coldDays++;
	}
	cout << coldDays << endl;
	return 0;
}
