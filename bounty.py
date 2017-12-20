#!/usr/bin/python
import sys
import os
import math
import bisect
import random

##start main with grabbing parameters and saving them off
UNIFORM_TRACES = sys.argv[1]

##read values in file into the random array/list for use later
S = []
n = 0
 
try:
    with open(UNIFORM_TRACES, "r") as file:
        for values in file:
            values = float(values)
            #print(values)
            S.append(values)
            n += 1
except IOError as e:
    print ("Could not open file: " + UNIFORM_TRACES)
    sys.exit(1)

S.sort()
def F(x): #the cdf function
    return (x+1)/n

def find_lt(a, x): #implicit binary searching using the bisect built in functionality of python
    j = bisect.bisect_left(a, x)
    if j:
        return j-1
    raise ValueError

def index(a, x):
    k = bisect.bisect_left(a, x)
    if k != len(a) and a[k] == x:
        return k
    raise ValueError

CDF = [0]*n
CDF[0] = F(0)
i = 0
while i < n:
    CDF[i] = F(i)
    i +=1
    
u = random.uniform(0,1)
x = find_lt(CDF,u)

#sx = index(CDF,x)

print("The random variate is: ", S[x])

