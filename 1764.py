import sys

N, M =  map(int, sys.stdin.readline().split())

nl = set()
ns = set()

for _ in range(N):
    nl.add(sys.stdin.readline().rstrip())

for _ in range(M):
    ns.add(sys.stdin.readline().rstrip())

nlns = list(nl & ns)
nlns.sort()

print(len(nlns))
for name in nlns:
    print(name)
