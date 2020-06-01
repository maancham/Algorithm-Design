class Graph():

    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for i in range(vertices)] for j in range(vertices)]

    def primMST(self):
        key = [10000000] * self.V
        parent = [None] * self.V
        key[0] = 0
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
                if self.graph[min_index][v] > 0 and key[v] > self.graph[min_index][v]:
                    if (mstSet[v]):
                        continue
                    else:
                        key[v] = self.graph[min_index][v]
                        dad[v] = min_index

        for i in range(1, self.V):
            x += self.graph[i][dad[i]]
        print(x)


n = int(input())
line = [[0 for i in range(n)] for j in range(n+1)]
for i in range(n+1):
    line[i] = list(map(int, input().split()))
for i in range(n):
    line[i].append(line[n][i])
line[n].append(0)

g = Graph(n+1)
g.graph = line

g.primMST()
