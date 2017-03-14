import random

DECK = [x for x in range(6)]

def pickMRecursively(cards,m, i):
    if (i +1) == m :
        return cards[:m]
    elif i +1 > m :
        subset = pickMRecursively(cards,m,i-1)
        k = random.randint(0, i)
        if (k < m):
            subset[k] = cards[i]
        return subset

    return None

def pickMIteratively(cards,m):
    lenC = len(cards)
    subset = cards[:m]
    for i in range(lenC):
        k = random.randint(0, i)
        if k < m :
            subset[k] = cards[i]

    return subset

if __name__ == '__main__':
    print DECK
    m = 3

    #subset = pickMRecursively(DECK,m,len(DECK))
    subset = []
    subset = pickMIteratively(DECK,m)
    print subset
