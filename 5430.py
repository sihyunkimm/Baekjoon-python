import sys
from collections import deque

T = int(sys.stdin.readline())

for _ in range(T):
    command_line = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    
    temp = sys.stdin.readline().rstrip()
    temp = temp[1:-1]
    
    if len(temp) == 0:
        num_deque = deque()
    else:        
        num_deque = deque(map(int, temp.split(',')))

    if command_line.count('D') > len(num_deque):
        print("error")
        continue

    rcnt = 0  #R count
    for command in command_line:
        if command == 'R':
            rcnt += 1
        else:
            if rcnt % 2 == 0:
                num_deque.popleft()
            else:
                num_deque.pop()
    if rcnt % 2 == 1:
        num_deque.reverse()

    print('[' + ','.join(map(str, num_deque)) +']')
