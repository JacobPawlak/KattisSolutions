//Jacob Pawlak
//November 13th, 2017
//Quick Brown Fox
//https://open.kattis.com/problems/quickbrownfox

#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){

	vector<char> alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	int num_phrases = 0;
	cin >> num_phrases;
	cin.ignore();
	for(int i = 0; i < num_phrases; i++){

		string phrase;
		getline(cin, phrase);

		for(int k = 0; k < phrase.length(); k++){
			phrase[k] = tolower(phrase[k]);

			int loc = -1;
			for(int p = 0; p < alphabet.size(); p++){
				if(alphabet[p] == phrase[k])
					loc = p;
			}
			if( (loc >= 0) && (loc < alphabet.size()) ){
				alphabet.erase(alphabet.begin() + loc -1);
			}
		}


		if(alphabet.size() == 0){
			cout << "pangram" << endl;
		}
		else{
			cout << "missing ";
			for(int j = 0; j < alphabet.size(); j++){
				cout << alphabet[j];
			}
			cout << endl;
		}

		alphabet = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'};
	}
}
