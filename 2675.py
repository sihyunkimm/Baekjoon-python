t = int(input())

for i in range(t):
    r, s = input().split()
    r = int(r)
    new =""
    
    for j in s:
        for k in range(r):
            new = new + j

    print(new) 