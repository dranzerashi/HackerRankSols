#!/bin/python3

"""
Question:
https://www.hackerrank.com/challenges/candies/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dynamic-programming
"""

import math
import os
import random
import re
import sys

# Complete the candies function below.
def candies(n, arr):
    data = [-1]*n
    data[0] = 1
    for i in range(1, n):
        if arr[i]>arr[i-1]:
            data[i] = data[i-1]+1
        else:
            j = i
            while data[j-2] > data[j-1]:
                data[i-1] += 1
                j -= 1
            data[i]=1 
    print(data)
    return sum(data)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = []

    for _ in range(n):
        arr_item = int(input())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
