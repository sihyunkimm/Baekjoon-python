import sys

input = sys.stdin.readline

K, N = map(int, input().split())

wires = [int(input()) for _ in range(K)]


start = 1
end = max(wires) + 1

while start + 1 < end:
    mid = (start + end) // 2 
    result = 0 

    for i in wires:
        result += i // mid 
        
    if result >= N: 
        start = mid
    else:
        end = mid

print(start)