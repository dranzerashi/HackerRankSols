#!/bin/python3

"""
Question
https://www.hackerrank.com/challenges/max-array-sum/problem?h_l=interview&playlist_slugs%5B%5D%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D%5B%5D=dynamic-programming&isFullScreen=true
"""

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.

def maxSubsetSum(arr):
    if len(arr) == 1:
        return arr[0]
    data = [None]*len(arr)
    data[0] = arr[0]
    data[1] = max(arr[0],arr[1])
    for i in range(2,len(arr)):
        data[i] = max(data[i-1],data[i-2],data[i-2]+arr[i],arr[i])
    return data[-1]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
