from math import comb
N = int(input())

answer = 0
for i in range(1, N//4+1):
    answer += (-1)**(i+1) * comb(13, i)  * comb(52-4*i, N-4*i) 

print(answer%10007)