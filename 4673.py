self_list = list(range(1,10001))

for i in range(1,10001):    
    num = str(i)
    gen = 0

    for i in range(len(num)):
        gen += int(num[i])

    gen += int(num)        

    if gen in self_list:
        self_list.remove(gen)

for i in self_list:
    print(i)