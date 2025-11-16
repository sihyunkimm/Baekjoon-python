import sys
from collections import deque

test_case = int(sys.stdin.readline())

for _ in range(test_case):
    N, M = map(int, sys.stdin.readline().split())
    q = deque(map(int, sys.stdin.readline().split()))
    doc_number = deque(range(N))
    count = 0

    while q:
        if q[0] >= max(q):
            count += 1
            q.popleft()
            number = doc_number.popleft()
            if number == M:
                print(count)
                break
        else:
            q.rotate(-1)
            doc_number.rotate(-1)

