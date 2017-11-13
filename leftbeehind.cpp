//Jacob Pawlak
//November 13th, 2017
//Left Beehind
//https://open.kattis.com/problems/leftbeehind


#include<iostream>

using namespace std;

int main(){

	int sweet, sour = 0;
	cin >> sweet;
	cin >> sour;

	while( (sweet > 0) || (sour > 0) ){

		if((sweet + sour) == 13){
			cout << "Never speak again." << endl;
		}

		else if(sweet > sour){
			cout << "To the convention." << endl;
		}

		else if(sweet < sour){
			cout << "Left beehind." << endl;
		}

		else {
			cout << "Undecided." << endl;
		}

		cin >> sweet;
		cin >> sour;

	}

}
