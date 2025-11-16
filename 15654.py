N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()

ans = []
def backtrack():
    if len(ans) == M:
        print(*ans)
        return 0

    for i in num_list:
        if i not in ans:
            ans.append(i)
            backtrack()
            ans.pop()

backtrack()
