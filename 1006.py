# https://casterian.net/ps/boj1006/ 참고

import sys
input = sys.stdin.readline
NULL = -1
INF = float('inf')

T = int(input())

for _ in range(T):
    N, W = map(int, input().split())
    e = list(list(map(int, input().split())) for _ in range(2))

    if N == 1:
        print(1 if e[0][0]+e[1][0] <= W else 2)
        continue

    a, b, c = [NULL for _ in range(N+1)], [NULL for _ in range(N+1)], [NULL for _ in range(N+1)]

    # 걸치지 않음
    a[0] = 0
    b[0] = 1
    c[0] = 1

    for i in range(N):
        a[i+1] = min(b[i]+1, c[i]+1)
        if e[0][i]+e[1][i] <= W:
            a[i+1] = min(a[i+1], a[i]+1)
        if i>0 and e[0][i-1]+e[0][i] <= W and e[1][i-1]+e[1][i] <= W:
            a[i+1] = min(a[i+1], a[i-1]+2)

        if i >= N-1:
            continue

        b[i+1] = a[i+1]+1
        if e[0][i]+e[0][i+1] <= W:
            b[i+1] = min(b[i+1], c[i]+1)
        
        c[i+1] = a[i+1]+1
        if e[1][i]+e[1][i+1] <= W:
            c[i+1] = min(c[i+1], b[i]+1)

    firstCaseAnswer = a[N]

    # 위 행만 걸침
    if e[0][-1]+e[0][0] <= W:
        a[0] = 0
        b[0] = 0
        c[0] = 1
        a[1] = 1
        b[1] = 2
        c[1] = 1 if e[1][0]+e[1][1] <= W else 2

        for i in range(1, N):
            a[i+1] = min(b[i]+1, c[i]+1)
            if e[0][i]+e[1][i] <= W:
                a[i+1] = min(a[i+1], a[i]+1)
            if i>0 and e[0][i-1]+e[0][i] <= W and e[1][i-1]+e[1][i] <= W:
                a[i+1] = min(a[i+1], a[i-1]+2)

            if i >= N-1:
                continue

            b[i+1] = a[i+1]+1
            if e[0][i]+e[0][i+1] <= W:
                b[i+1] = min(b[i+1], c[i]+1)
            
            c[i+1] = a[i+1]+1
            if e[1][i]+e[1][i+1] <= W:
                c[i+1] = min(c[i+1], b[i]+1)
        
        secondCaseAnswer = c[N-1] + 1
    else:
        secondCaseAnswer = INF

    # 아래 행만 걸침
    if e[1][-1]+e[1][0] <= W:
        a[0] = 0
        b[0] = 1
        c[0] = 0
        a[1] = 1
        b[1] = 1 if e[0][0]+e[0][1] <= W else 2
        c[1] = 2

        for i in range(1, N):
            a[i+1] = min(b[i]+1, c[i]+1)
            if e[0][i]+e[1][i] <= W:
                a[i+1] = min(a[i+1], a[i]+1)
            if i>0 and e[0][i-1]+e[0][i] <= W and e[1][i-1]+e[1][i] <= W:
                a[i+1] = min(a[i+1], a[i-1]+2)

            if i >= N-1:
                continue

            b[i+1] = a[i+1]+1
            if e[0][i]+e[0][i+1] <= W:
                b[i+1] = min(b[i+1], c[i]+1)
            
            c[i+1] = a[i+1]+1
            if e[1][i]+e[1][i+1] <= W:
                c[i+1] = min(c[i+1], b[i]+1)

        thirdCaseAnswer = b[N-1] + 1
    else:
        thirdCaseAnswer = INF

    # 두 행 다 걸침
    if e[0][-1]+e[0][0] <= W and e[1][-1]+e[1][0] <= W:
        a[0] = 0
        b[0] = 0
        c[0] = 0
        a[1] = 0
        b[1] = 1
        c[1] = 1

        for i in range(1, N):
            a[i+1] = min(b[i]+1, c[i]+1)
            if e[0][i]+e[1][i] <= W:
                a[i+1] = min(a[i+1], a[i]+1)
            if i>0 and e[0][i-1]+e[0][i] <= W and e[1][i-1]+e[1][i] <= W:
                a[i+1] = min(a[i+1], a[i-1]+2)

            if i >= N-1:
                continue

            b[i+1] = a[i+1]+1
            if e[0][i]+e[0][i+1] <= W:
                b[i+1] = min(b[i+1], c[i]+1)
            
            c[i+1] = a[i+1]+1
            if e[1][i]+e[1][i+1] <= W:
                c[i+1] = min(c[i+1], b[i]+1)

        fourthCaseAnswer = a[N-1] + 2
    else:
        fourthCaseAnswer = INF

    print(min(firstCaseAnswer, secondCaseAnswer, thirdCaseAnswer, fourthCaseAnswer))