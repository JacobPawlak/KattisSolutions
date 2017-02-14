//Jacob Pawlak
//February 14th, 2017 Happy Valentines Day!
//Speed Limit
//https://open.kattis.com/problems/speedlimit

#include<iostream>

using namespace std;

int main(){

	int records = 0;
	cin >> records;
	while(records != -1){

		int total_miles = 0;
		int prev_time = 0;
		for(int i = 0; i < records; i++){

			int speed, time_h = 0;
			cin >> speed >> time_h;
			total_miles += speed * (time_h - prev_time);
			prev_time = time_h;

		}

		cout << total_miles << " miles" << endl;

		cin >> records;

	}

	return 0;
}
