#!/bin/python

import math
import os
import random
import re
import sys

if __name__ == '__main__':
    s = raw_input()
    alpha = [chr(i) for i in range(65, 91)] + [chr(i) for i in range(97, 123)]

    counts = list()
    final = list()
    count = 1

    for i in alpha:
        counts.append(s.count(i))

    while count < 4:
        temp_lis = []
        temp = max(counts)
        temp_idx = counts.index(temp)
        temp_lis.append(alpha[temp_idx])
        temp_lis.append(counts[temp_idx])
        final.append(temp_lis)
        alpha.remove(alpha[temp_idx])
        counts.remove(counts[temp_idx])
        count = count + 1

    for i in final:
        for j in i:
            print(j),
        print("\r")


