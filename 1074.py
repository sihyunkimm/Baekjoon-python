import sys


# devide and conquer
def dNc(r, c, size, value):

    mid = size//2
    
    if r < mid and c < mid:
        if mid == 1:
            print(value)
            return 0
        else:
            dNc(r, c, mid, value)
            
    elif r < mid and c >= mid:
        if mid == 1:
            print(value + 1)
            return 0
        else:
            dNc(r, c - mid, mid, value + mid**2)

    elif r >= mid and c < mid:
        if mid == 1:
            print(value + 2)
            return 0
        else:
            dNc(r - mid, c, mid, value + mid**2 * 2)

    elif r >= mid and c >= mid:
        if mid == 1:
            print(value + 3)
            return 0
        else:
            dNc(r - mid, c - mid, mid, value + mid**2 * 3)


N, R, C = map(int, sys.stdin.readline().split())
dNc(R, C, 2**N, 0)
