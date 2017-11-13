//Jacob Pawlak
//November 13th, 2017
//Simon Says
//https://open.kattis.com/problems/simonsays


#include<iostream>
#include<string>

using namespace std;

int main(){

	int num_phrases = 0;
	cin >> num_phrases;
	for(int i = 0; i < (num_phrases + 1); i++){

		string phrase;
		getline(cin, phrase);
		string ss_bit = phrase.substr(0, 10);
		if(ss_bit == "Simon says"){
			cout << phrase.substr(11, phrase.length() - 1) << endl;
		}

	}

	return 0;

}
