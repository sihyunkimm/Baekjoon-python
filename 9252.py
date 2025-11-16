first_str = input()
second_str = input()

lcs_num = list(list(0 for _ in range(len(second_str) + 1)) for _ in range(len(first_str) + 1))
lcs_str = list(list('' for _ in range(len(second_str) + 1)) for _ in range(len(first_str) + 1))

for i in range(1, len(first_str) + 1):
    for j in range(1, len(second_str) + 1):
        if first_str[i-1] == second_str[j-1]:
            lcs_num[i][j] = lcs_num[i-1][j-1] + 1
            lcs_str[i][j] = lcs_str[i-1][j-1] + first_str[i-1]
        elif lcs_num[i-1][j] >= lcs_num[i][j-1]:
            lcs_num[i][j] = lcs_num[i-1][j]
            lcs_str[i][j] = lcs_str[i-1][j]
        else:
            lcs_num[i][j] = lcs_num[i][j-1]
            lcs_str[i][j] = lcs_str[i][j-1]

print(lcs_num[-1][-1])
if lcs_num[-1][-1] != 0:
    print(lcs_str[-1][-1])
            