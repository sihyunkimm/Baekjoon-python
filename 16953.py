from collections import deque

MAX = 10**9

A, B = map(int, input().split())

dst_dict = {A:1}

q = deque()
q.append(A)

dst = 1
while q:
    dst += 1
    for _ in range(len(q)):
        current = q.popleft()
        doubled = current * 2
        addone = int(str(current) + '1')
        if doubled <= MAX and doubled not in dst_dict:
            dst_dict[doubled] = dst
            q.append(doubled)
        if addone <= MAX and addone not in dst_dict:
            dst_dict[addone] = dst
            q.append(addone)

if B in dst_dict:
    print(dst_dict[B])
else:
    print(-1)
