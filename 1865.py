import sys

input = sys.stdin.readline
INF = 100000

TC = int(input())

for _ in range(TC):
    N, M, W = map(int, input().split())
    edges = []
    
    for _ in range(M):
        S, E, T = map(int, input().split())
        edges.append([S, E, T])
        edges.append([E, S, T])

    for _ in range(W):
        S, E, T = map(int, input().split())
        edges.append([S, E, -T])
        
    def bellman():
        distance = [INF] * (N+1)
        distance[1] = 0
        
        for i in range(N):
            for e in edges:
                mid, end, dist = e
                if distance[end] > distance[mid] + dist:
                    distance[end] = distance[mid] + dist
                    if i == N-1:
                        print("YES")
                        return

        print("NO")
        return        
    
    bellman()