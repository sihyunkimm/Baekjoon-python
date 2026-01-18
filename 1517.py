import sys
input = sys.stdin.readline

N = int(input())
num_list = list(map(int, input().split()))
answer = 0

def merge_sort(start, end):
    global answer, num_list
    if start < end:
        mid = (start + end) // 2
        merge_sort(start, mid)
        merge_sort(mid+1, end)

        temp = []
        x, y = start, mid+1
        while x <= mid and y <= end:
            if num_list[x] <= num_list[y]:
                temp.append(num_list[x])
                x += 1
            else:
                temp.append(num_list[y])
                y += 1
                answer += (mid - x) + 1

        if x <= mid:
            temp = temp + num_list[x:mid+1]
        if y <= end:
            temp = temp + num_list[y:end+1]

        for i in range(len(temp)):
            num_list[start+i] = temp[i]
        
merge_sort(0, N-1)
print(answer)