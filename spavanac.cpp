//Jacob Pawlak
//February 14th, 2017 Happy Valentines day!
//Spavanac
//https://open.kattis.com/problems/spavanac

#include<iostream>

using namespace std;

int main(){

	int hours, mins = 0;
	cin >> hours >> mins;
	mins -= 45;
	if(mins < 0){
		mins += 60;
		hours--;
		if(hours < 0)
			hours = 23;

	}

	cout << hours << " " << mins << endl;
	return 0;
}
