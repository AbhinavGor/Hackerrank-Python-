####^^^^THIS GIVES RUNTIME ERROR FOR A VERY LONG STRING^^^^####
#from itertools import *

#string = str(input())

#for key, group in groupby(string, key=lambda x: x[0]):
#    temp = 0
#    for thing in group:
#        temp = temp + 1

#    print ("(%d, %d)" % (int(temp), int(key))),

####EFFICIENT CODE####

import itertools

S = input()

for key, group in itertools.groupby(S):
    print (len(list(group)), int(k)),