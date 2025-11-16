from collections import deque

num_pc = int(input())
num_line = int(input())

lines = []

for i in range(num_line):
    lines.append(list(map(int, input().split())))

q = deque()
q.append(1)

visited = set()
visited.add(1)

while q:
    for i in range(len(q)):
        pc = q.popleft()       
        for line in lines:
            if pc in line and line[1-line.index(pc)] not in visited:
                #print(line)
                q.append(line[1-line.index(pc)])
                visited.add(line[1-line.index(pc)])

        #print(q)

print(len(visited) - 1)
