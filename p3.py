#!/usr/bin/python
import math
import sys
import numpy as np
from statistics import mean

N = 1000
i = 0
passing = 0

def generate():
    u = math.floor(np.random.uniform(1, 21))
    #print(u)
    ex1 = 4*.5 + 3*.3 + 2*.2
    ex2 = 3*.1 + 2*.3 + 1*.4
    X = u*ex1 + u*ex2
    #print(X)
    if X > 50:
        return 1
    else:
        return 0
    
def sim():
    x_bar = generate()
    n = 1
    t = 2.63
    v = 0
    while(n < 100):# or 0.03 < (t/math.sqrt(n-1))):
        x = generate()
        n += 1
        d = x - x_bar
        v = v + ((n-1)/n)*d**2
        x_bar += (d/n)
    s= math.sqrt(v/n)
    return x_bar


Y = []
while i < N:
    y =  sim() # probability of passing
    print(i, y)
    i +=1
    Y.append(y)

print(mean(Y))
