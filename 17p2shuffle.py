import random
import itertools
import math
import random
SUITS = 'cdhs'
RANKS = '23456789TJQKA'
DECK = list(''.join(card) for card in itertools.product(RANKS, SUITS))

def shuffleArrayRecursively(cards,i):
    if (i == 0) :
        return cards
    shuffleArrayRecursively(cards,i-1)
    k = random.randint(0,i)

    cards[k],cards[i] = cards[i],cards[k]

    return cards

def shuffleArrayIteratively(cards):
    lenC = len(cards)
    for i in range(lenC):
        k = random.randint(0, i)

        cards[k], cards[i] = cards[i], cards[k]
    return cards

if __name__ == '__main__':
    print DECK
    print len(DECK)
    shuffleArrayRecursively(DECK,51)
    print DECK
    shuffleArrayIteratively(DECK)
    print DECK
