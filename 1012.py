from collections import deque
import sys


directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]


#main
T = int(sys.stdin.readline())

for _ in range(T):
    M, N, K = map(int, sys.stdin.readline().split())
    
    cabs = set()
    for i in range(K):
        c, r = map(int, sys.stdin.readline().split())
        cabs.add((r, c))

    count = 0    
    q = deque()
    while cabs:
        q.append(cabs.pop())
                
        while q:
            rc = q.popleft()
            
            for d in directions:
                nr = rc[0] + d[0]
                nc = rc[1] + d[1]        
                if 0 <= nr < N and 0 <= nc < M and (nr, nc) in cabs:
                    cabs.remove((nr, nc))
                    q.append((nr, nc))
      
        count += 1
        
    
    print(count)
