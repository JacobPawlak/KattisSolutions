//Jacob Pawlak
//November 12th, 2017
//Volim
//https://open.kattis.com/problems/volim

#include<iostream>

using namespace std;

int main(){

	int seat, questions, bad_seat = 0;
	int bomb_time = 210;
	int time_used = 0;
	cin >> seat;
	//seat has to be bound between 1 and 8
	cin >> questions;
	for(int i = 0; i < questions; i++){

		int seconds = 0;
		char answer;
		cin >> seconds >> answer;
		if(time_used >= bomb_time){
			cout << "tripped" << endl;
			bad_seat = seat;
			continue;

		}
		else{

			time_used += seconds;
			cout << "Time used: " << time_used << "   bomb time: " << bomb_time << endl;
			if(answer == 'T'){
				if(seat == 8)
					seat = 1;
				else
					seat++;
			}
			cout << "Seat: " << seat << "   bad_seat: " << bad_seat  << endl;

		}

	}
	cout << bad_seat << endl;

}
