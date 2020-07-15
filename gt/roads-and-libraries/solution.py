#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the roadsAndLibraries function below.
def build_graph(n, cities):
    g = {i:[] for i in range(1,n+1)}
    for (s,e) in cities:
        g[s].append(e)
        g[e].append(s)
    return g

def roadsAndLibraries(n, c_lib, c_road, cities):
    if c_lib < c_road:
        return n * c_lib
    road_network = build_graph(n, cities)
    disjoint_cities = 0
    rebuild_roads = 0
    visited = {i:False for i in range(1,n+1)}
    for i in range(1,n+1):
        if not visited[i]:
            #print(road_network)
            #print(visited)
            disjoint_cities+=1
            queue = [i]
            while(len(queue)>0):
                c = queue.pop(0)
                visited[c] = True
                for ct in road_network[c]:
                    if not visited[ct] and ct not in queue:
                        queue.append(ct)
                        rebuild_roads+=1
    print(rebuild_roads, disjoint_cities)
    return rebuild_roads*c_road + disjoint_cities * c_lib

if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        nmC_libC_road = input().split()

        n = int(nmC_libC_road[0])

        m = int(nmC_libC_road[1])

        c_lib = int(nmC_libC_road[2])

        c_road = int(nmC_libC_road[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        print(str(result) + '\n')

