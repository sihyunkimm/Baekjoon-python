from collections import deque
import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    start, end = map(int,input().split())
    visited = [False for _ in range(10001)]
    q = deque()
    q.append([start, ''])
    visited[start] = True
    
    while q:
        num, command = q.popleft()
        if num == end:
            print(command)
            break
        d = num*2 % 10000
        s = (num-1) % 10000
        l = num*10%10000 + num//1000
        r = num//10 + num%10*1000

        if not visited[d]:
            visited[d] = True
            q.append([d, command + 'D'])

        if not visited[s]:
            visited[s] = True
            q.append([s, command + 'S'])

        if not visited[l]:
            visited[l] = True
            q.append([l, command + 'L'])

        if not visited[r]:
            visited[r] = True
            q.append([r, command + 'R'])
            