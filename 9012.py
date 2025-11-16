import sys

N = int(sys.stdin.readline())

for _ in range(N):
    vps = sys.stdin.readline().rstrip()
    
    l = 0
    r = 0
    for i in vps:
        if i == '(':
            l += 1
        elif i == ')':
            r += 1

        if r > l:
            print('NO')
            break
    else:
        if l == r:
            print('YES')
        else:
            print('NO')
