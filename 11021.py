case = int(input())

for i in range(case):
    a,b = input().split()
    a = int(a)
    b = int(b)
    print("Case #", (i+1), ": ", a+b, sep="")