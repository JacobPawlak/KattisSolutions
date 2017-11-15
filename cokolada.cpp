//Jacob Pawlak
//November 14th, 2017
//Cokolada
//https://open.kattis.com/problems/cokolada

#include<iostream>
#include<string>
#include<cmath>

using namespace std;

int main(){

	int k_pieces, smallest_bar, num_breaks = 0;
	cin >> k_pieces;

	for(int i = 0; i < k_pieces; i++){
		if(pow(2, i) >= k_pieces){
			smallest_bar = pow(2,i);
			break;
		}
	}

	int pieces = 0;

	for(int j = 1; j < k_pieces; j++){
		if(pieces >= k_pieces){
			num_breaks = j;
			break;
		}
		else{
			pieces += (smallest_bar / pow(2, j));
		}
	}

	cout << smallest_bar << " " << num_breaks << endl;
	return 0;
}
