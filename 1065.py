def han(a):
    num = str(a)
    is_true = True

    if a < 10:
        dif = a
    else:
        dif = int(num[0]) - int(num[1])

    for i in range(len(num)-1):
        a = int(num[i])
        b = int(num[i+1])
        if dif != a - b:
            is_true = False    

    if is_true:
        return True
    else:
        return False


n = int(input())
cnt = 0

for i in range(1,n+1):
    if han(i):
        cnt += 1
    
print(cnt)