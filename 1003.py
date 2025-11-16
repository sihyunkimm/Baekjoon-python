import sys

f_dic = {
    # fibonacci(n) : (value, 0 count, 1 count)
    0 : (0, 1, 0),
    1 : (1, 0, 1)
}

def fibonacci(n, dic):
    if n in dic:
        return dic[n]
    else:
        f1 = fibonacci(n-1, dic)
        f2 = fibonacci(n-2, dic)
        dic[n] = (f1[0]+f2[0], f1[1]+f2[1], f1[2]+f2[2]) 
        return dic[n]

T = int(sys.stdin.readline())

for i in range(T):
    n = int(sys.stdin.readline())
    result = fibonacci(n, f_dic)
    print(result[1], result[2])   

#print(f_dic)

