T = int(input())

num_cases = [1, 2, 4]

for i in range(3, 11):
    num_cases.append(sum(num_cases[i-3:i]))

for i in range(T):
    n = int(input())
    print(num_cases[n-1])
