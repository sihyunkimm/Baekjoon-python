N, M = map(int, input().split())
numbers = sorted(list(map(int, input().split())))


visited = [False] * N 
answer = []

def back():
    last = 0
    if len(answer) == M:
        print(*answer)
        return 0

    for i in range(N):
        current = numbers[i]
        if last != current and visited[i] == False:
            answer.append(current)
            last = current
            visited[i] = True    
            
            back()
            
            answer.pop()
            visited[i] = False

back()
