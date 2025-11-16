r = 31
M = 1234567891

L = int(input())

to_hash = input()

sum = 0
for i in range(L):
    sum += (ord(to_hash[i]) - ord('a') + 1) * (r**i)

print(sum % M)
