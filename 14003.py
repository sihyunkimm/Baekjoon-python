N = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]  # lis[i] 는 i+1 길이의 부분 수열의 마지막 원소 중 가장 작은 원소를 나타냄
indexes = []  # index[i] 는 arr[i] 가 lis 에서 위치하는 인덱스를 나타냄

def biSearch(n):
    if n > lis[-1]:
        return -1
    
    start, end = 0, len(lis) - 1
    while start <= end:
        mid = (start + end) // 2
        
        if n == lis[mid]:
            return mid
        elif n < lis[mid]:
            end = mid - 1
        else:
            start = mid + 1
            
    return start

for n in arr:
    index = biSearch(n)
    if index == -1:
        lis.append(n)
        indexes.append(len(lis) - 1)
    else:
        lis[index] = n
        indexes.append(index)

print(len(lis))

answer = []
index_to_find = len(lis) - 1
for i in range(len(indexes) -1 , -1, -1):
    if indexes[i] == index_to_find:
        answer.append(arr[i])
        index_to_find -= 1

print(*reversed(answer))