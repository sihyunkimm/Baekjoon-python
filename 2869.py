A, B, V = map(int, input().split())

day = -1
if V <= A:
    day = 1
elif V - (A - B) <= A:
    day = 2
elif (V-A) % (A-B) == 0: 
    day = (V-A) // (A-B) + 1
else:
    day = (V-A) // (A-B) + 2
    
print(day)
