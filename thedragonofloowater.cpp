//Jacob Pawlak
//November 14th, 2017
//The dragon of Loowater
//https://open.kattis.com/problems/loowater

#include<iostream>
#include<cmath>
#include<algorithm>
#include<vector>

using namespace std;

int main(){

	int num_dragons, num_knights = 0;
	cin >> num_dragons;
	cin >> num_knights;

	while( (num_dragons > 0) || (num_knights > 0) ){

		vector<int> dragon_heads;
		vector<int> knight_heights;

		if(num_knights < num_dragons){
			for(int i = 0; i < num_dragons; i++){
                                int head_diam = 0;
                                cin >> head_diam;
                                dragon_heads.push_back(head_diam);
                        }
                        for(int j = 0; j < num_knights; j++){
                                int knight_h = 0;
                                cin >> knight_h;
                                knight_heights.push_back(knight_h);
                        }
			cout << "Loowater is doomed!" << endl;
		}
		else{
			for(int i = 0; i < num_dragons; i++){
				int head_diam = 0;
				cin >> head_diam;
				dragon_heads.push_back(head_diam);
			}
			for(int j = 0; j < num_knights; j++){
				int knight_h = 0;
				cin >> knight_h;
				knight_heights.push_back(knight_h);
			}
			sort(dragon_heads.begin(), dragon_heads.end());
			sort(knight_heights.begin(), knight_heights.begin());
			/*
			for(int k = 0; k < dragon_heads.size(); k++){
				cout << dragon_heads[k] << " ";
			}
			cout << endl;
			for(int k = 0; k < knight_heights.size(); k++){
				cout << knight_heights[k] << " ";
			}
			cout << endl;
			*/
			for(int k = 0; k < dragon_heads.size(); k++){
				for(int l = 0; l < knight_heights.size(); l++){
					
				}
			}
		}

		cin >> num_dragons;
		cin >> num_knights;

	}

	return 0;
}
