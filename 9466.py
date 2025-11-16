import sys

input = sys.stdin.readline

testcase = int(input())

for _ in range(testcase):
    total_student = int(input())
    choices = [0] + list(map(int, input().split()))
    visited = [False] * (total_student + 1)
    failure = [False] * (total_student + 1)

    for start in range(1, total_student + 1):
        if visited[start] == True:
            continue

        if choices[start] == start:
            visited[start] = True
            continue

        loop = [start]
        visited[start] = True
        current = start
        while True:
            current = choices[current]
            if current == start:
                break
            elif visited[current] == True:
                for i in loop:
                    if i != current:
                        failure[i] = True
                    else:
                        break
                break
            else:
                loop.append(current)
                visited[current] = True

    cnt = 0
    for i in failure:
        if i:
            cnt += 1
    print(cnt)
