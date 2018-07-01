// Cards.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include "Cards.h"
using namespace std;

int main(){
    Deck deck;
    deck.shuffle();
    vector<Card> vc = deck.deal_hand(5);
    cout<<deck.remain_cards()<<endl;
    for(int i=0; i< static_cast<int>(vc.size()); ++i)
        cout<<vc[i].value()<<" "<<(Suit)vc[i].suit()<<endl;
	int var1;
	cin >> var1;
    return 0;
}
