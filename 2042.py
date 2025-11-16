import sys
sys.setrecursionlimit(10 ** 8)

N, M, K = map(int, input().split())

arr = [0]
for _ in range(N):
    arr.append(int(input()))
tree = [0] * (4*N)

def makeTree(cur_node, start, end):
    if start == end:
        tree[cur_node] = arr[end]
        return tree[cur_node]
    
    mid = (start + end) // 2
    tree[cur_node] = makeTree(cur_node * 2, start, mid) + makeTree(cur_node * 2 + 1, mid + 1, end)    
    return tree[cur_node]


def subsum(cur_node, start, end, left, right):  # cur_node, start, end 는 현재 노드와 노드의 계산 범위, left와 right 는 계산하고자 하는 범위
    if end < left or start > right:
        return 0
    
    if left <= start and end <= right:
        return tree[cur_node]
    
    mid = (start + end) // 2
    return subsum(cur_node*2, start, mid, left, right) + subsum(cur_node*2+1, mid+1, end, left, right)
    
    
def updateTree(cur_node, start, end, target_idx, value):
    if target_idx < start or target_idx > end:
        return
    
    if start == end:
        tree[cur_node] = value
        return
    
    mid = (start + end) // 2
    updateTree(cur_node*2, start, mid, target_idx, value)
    updateTree(cur_node*2+1, mid+1, end, target_idx, value)
    tree[cur_node] = tree[cur_node*2] + tree[cur_node*2+1]
    return


makeTree(1, 1, N)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    if a == 1:
        updateTree(1, 1, N, b, c)
    else:
        print(subsum(1, 1, N, b, c))
