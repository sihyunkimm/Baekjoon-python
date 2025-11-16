N = int(input())

fkg = N // 5
tkg = (N - fkg*5) // 3

while N - (fkg*5 + tkg*3) != 0:
    fkg -= 1
    if fkg < 0:
        print(-1)
        exit()
    tkg = (N - fkg*5) // 3

print(fkg + tkg)
