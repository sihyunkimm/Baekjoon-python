N, M = map(int, input().split())

arr = [0]
for _ in range(N):
    arr.append(int(input()))

tree = [[0, 0] for _ in range(4*N)]

def makeTree(cur_node, start, end):
    if start == end:
        tree[cur_node] = [arr[start], arr[start]]
        return tree[cur_node]
    
    mid = (start + end) // 2
    child_a = makeTree(cur_node*2, start, mid)
    child_b = makeTree(cur_node*2+1, mid+1, end)
    tree[cur_node] = [min(child_a[0], child_b[0]), max(child_a[1], child_b[1])]
    return tree[cur_node]

def findMinMax(cur_node, start, end, left, right):
    if end < left or right < start:
        return [0, 0]
    pass

    if left <= start and end <= right:
        return tree[cur_node]
    
    mid = (start + end) // 2
    return_a = findMinMax(cur_node*2, start, mid, left, right)
    return_b = findMinMax(cur_node*2+1, mid+1, end, left, right)

    if return_a == [0, 0]:
        return return_b
    elif return_b == [0, 0]:
        return return_a
    else:
        return [min(return_a[0], return_b[0]), max(return_a[1], return_b[1])]

makeTree(1, 1, N)

for _ in range(M):
    a, b = map(int, input().split())
    answer = findMinMax(1, 1, N, a, b)
    print(answer[0], answer[1])