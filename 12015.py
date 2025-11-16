N = int(input())
arr = list(map(int, input().split()))

lis = [arr[0]]  # lis[i] 는 i+1 길이의 부분 수열의 마지막 원소 중 가장 작은 원소를 나타냄

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
    else:
        lis[index] = n

print(len(lis))