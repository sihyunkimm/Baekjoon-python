import sys

sys.setrecursionlimit(10**8) 

input = sys.stdin.readline 


n = int(input())

tree = {}
for i in range(n):
    root, left, right = map(str, input().split()) 
    tree[root] = left, right  # {'A': ('B', 'C')}


def preorder(v):  # 전위순회
    if v != ".":  # 루트 노트가 .이 아니면
        print(v, end="")
        preorder(tree[v][0])  # 재귀적으로 왼쪽 노드 탐색
        preorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색
    return


def inorder(v):  # 중위순회
    if v != ".":  # .이 아니면
        inorder(tree[v][0])  # 재귀적으로 왼쪽 노드 탐색
        print(v, end="")  # 루트 출력
        inorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색
    return


def postorder(v):  # 후위순회
    if v != ".":  # .이 아니면
        postorder(tree[v][0])  # 재귀적으로 왼쪽 노드 탐색
        postorder(tree[v][1])  # 재귀적으로 오른쪽 노드 탐색
        print(v, end="")  # 루트 출력
    return


preorder('A')
print()
inorder('A')
print()
postorder('A')