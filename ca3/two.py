import numpy as np


class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]

    def primMST(self, source, destination):
        key = [10000000] * self.V
        dad = [None] * self.V
        key[source] = 0
        mstSet = [False] * self.V
        x = 0
        dad[0] = -1

        for i in range(self.V):
            min = 10000000
            min_index = 0
            for v in range(self.V):
                if (key[v] < min):
                    if (mstSet[v]):
                        continue
                    else:
                        min = key[v]
                        min_index = v
            mstSet[min_index] = True
            for v in range(self.V):
                if self.graph[min_index][v] > 0 and key[v] > (self.graph[min_index][v] + key[min_index]):
                    if (mstSet[v]):
                        continue
                    else:
                        key[v] = self.graph[min_index][v] + key[min_index]
                        dad[v] = min_index

        print(key[destination])


size = 150
matrix = [[0 for i in range(size)] for j in range(size)]
first_line = list(map(int, input().split()))
n = first_line[0]
s = first_line[1]
t = first_line[2]
for i in range(n):
    line = list(map(int, input().split()))
    line = line[1:]
    line.sort()
    for j in range(len(line) - 1):
        matrix[line[j]][line[j+1]] = line[j+1] - line[j]
        matrix[line[j+1]][line[j]] = line[j+1] - line[j]

g = Graph(size)
g.graph = matrix

g.primMST(s, t)
