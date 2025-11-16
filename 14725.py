import sys

input = sys.stdin.readline

N = int(input())
ant_hill = {}

for _ in range(N):
    food_list = list(input().rstrip().split())
    deep = int(food_list[0])

    parent = ant_hill

    for i in range(1, deep + 1):
        food = food_list[i]
        if food not in parent:
            parent[food] = {}

        parent = parent[food]


def recursive_print(parent, cur_layer):
    keys = sorted(parent)

    for key in keys:
        print('--'*cur_layer + key)
        
        if len(parent[key]) > 0:
            recursive_print(parent[key], cur_layer+1)


recursive_print(ant_hill, 0)