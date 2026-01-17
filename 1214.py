D, P, Q = map(int, input().split())

if P < Q:
    P, Q = Q, P

if D%P == 0 or D%Q == 0:
    print(D)
    exit(0)

min_diff = 1e9
for i in range(min(D//P, Q)+1):
    min_diff = min(min_diff,(Q - (D - P*i) % Q) % Q)
min_diff = min(min_diff,(P - D%P) % P)

print(D+min_diff)