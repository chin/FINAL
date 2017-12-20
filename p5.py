#!/usr/bin/python
import sys
import os
import math
import numpy as np
from statistics import mean
from statistics import stdev
import matplotlib.pyplot as plt

N = 1000 #number of simulations

cards_rem = []
n = 0

def sim():
    #create deck of cards
    deck = []
    hand = []
    Suits = ['C', 'D', 'H', 'S']
    for v in range(1,14):
        for s in Suits:
            deck.append( (s,v) )

    #shuffle the deck
    np.random.shuffle(deck)
 
    #Cards are shuffled and put face down on table    
    hand.extend(deck[:4])
    #print(hand)
    deck = deck[4:]

    #print(str(hand[0].suit))
    while deck != []:
        while len(hand) < 4 and deck != []: #add card until we know there are at least 4 in hand
            hand.extend( deck[:1] )
            deck = deck[1:]
        #first and fourth
        if len(hand) >= 4:
            s1, v1 = hand[-4]
            s4, v4 = hand[-1] 
            if s1 is s4:
                hand.remove( hand[-2] ) #second card
                hand.remove( hand[-2] ) #third card
            elif v1 == v4:
                hand.remove( hand[-1] ) #fourth card
                hand.remove( hand[-1] ) #third card
                hand.remove( hand[-1] ) #second card
                hand.remove( hand[-1] ) #first card
            else:
                hand.extend( deck[:1] )
                deck = deck[1:]
    cards_rem.extend(hand)
    return len(hand)
    # n +=1


rem = []
while n < N:
    x = sim()
    rem.append(x)
    print(x)
    n += 1

print("got here")
rem.sort()
print( "Sample mean of remaining cards: ", mean(rem) )
print( "Sample standard deviation of remaining cards: ", stdev(rem) )
    
#N, bins = np.histogram(rem)
#plt.hist(rem, normed=True, bins='auto')
#plt.title('Histogram of cards remaining')
#plt.xlabel('No. Cards Remaining')
#plt.ylabel('Frequency')
#plt.grid(True)
#plt.show()
