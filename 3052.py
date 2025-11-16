num_list = []
rem_list = []

for i in range(10):
    num_list.append(int(input()))

for i in num_list:
    rem = i%42
    if rem in rem_list:
        pass
    else:
        rem_list.append(rem)

print(len(rem_list))