from collections import defaultdict 
import numpy as np


row = 0
def BFS(s, t, parent,graph): 
	visited =[False]*(row) 
	queue=[] 
	queue.append(s) 
	visited[s] = True
	while queue: 
		u = queue.pop(0) 
		for ind, val in enumerate(graph[u]): 
			if visited[ind] == False and val > 0 : 
				queue.append(ind) 
				visited[ind] = True
				parent[ind] = u
	if (visited[t]):
	    return True
	else:
	    return False

def make_change(graph,sign,value,a,b):
    if(sign == '+'):
        graph[a][b] += value
    else:
        graph[a][b] -= value
    return graph
		
def FordFulkerson(source, sink, graph): 
	parent = [-1]*(row) 
	max_flow = 0
	while BFS(source, sink, parent,graph) : 
		flow = 9999999999 
		s = sink 
		while(s != source): 
			flow = min (flow, graph[parent[s]][s]) 
			s = parent[s] 
		max_flow += flow 
		v = sink 
		while(v != source): 
			u = parent[v] 
			graph = make_change(graph,'-',flow,u,v)
			graph = make_change(graph,'+',flow,v,u)
			v = parent[v] 
	return max_flow 




first_line = list(map(int, input().split()))
n = first_line[0]
m = first_line[1]
c = first_line[2]
size = n+m+2
matrix = [[0 for i in range(size)] for j in range(size)]
for i in range(m):
    line = list(map(int, input().split()))
    line.pop(0)
    for j in range(len(line)):
        matrix[i+1][m+1+line[j]] = 1

for i in range(n):
    matrix[m+i+1][size-1] = c
for i in range(m):
    matrix[0][i+1] = 1

source = 0
sink = n + m + 1
row = len(matrix)
print (FordFulkerson(source, sink, matrix))
