import sys
import heapq

V,E = map(int,sys.stdin.readline().split()) 
K = int(sys.stdin.readline())

graph = [[] for _ in range(V+1)]
INF = float('inf') 

distance = [INF] * (V+1)
distance[K] = 0 


for _ in range(E):
    u, v, w = map(int,sys.stdin.readline().split())
    graph[u].append((v,w))


visited = [False] * (V+1)
heap = []
heapq.heappush(heap,(0,K))

while heap:
    min_dis, cur_node = heapq.heappop(heap)        
    if visited[cur_node]:
        continue
   
    visited[cur_node] = True
   
    for node,dis in graph[cur_node]:
        new_d = min_dis+dis

        if new_d < distance[node]:
            distance[node] = new_d
            heapq.heappush(heap,(new_d,node))


for idx in range(1,len(distance)):
    if distance[idx] == INF:
        print('INF')
    else:
        print(distance[idx])