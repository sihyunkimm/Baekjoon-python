case = int(input())


for i in range(case):
    score = 0
    temp = 0
    result = input()

    for i in range(len(result)):
        tempResult = result[i]
        
        if tempResult == "O":
            temp = temp + 1
            score = score + temp  
        elif tempResult == "X":
            temp = 0
        else:
            print("something is wrong")
        
        # print(temp)

    print(score)    