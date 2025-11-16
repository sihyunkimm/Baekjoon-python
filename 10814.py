N = int(input())

age_name = []

for _ in range(N):
    age_name.append(list(input().split()))

age_name.sort(key = lambda x:int(x[0]))

for an in age_name:
    print(*an)
