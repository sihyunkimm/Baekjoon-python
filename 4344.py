c = int(input())


for i in range(c):
    total = 0
    scoreList = list(map(int, input().split()))
    new_list = []
    
    stdNum = scoreList[0]
    del scoreList[0]

    for i in scoreList:
        total = total + i

    # print(total)

    average = total / stdNum

    # print(average)

    # print(scoreList[0])

    for i in range(stdNum):
        # print(i)
        # print(scoreList[i])

        if scoreList[i] > average:
            new_list.append(scoreList[i])

    # print(new_list)

    per = len(new_list) / stdNum * 100

    print(format(per, ".3f"), "%", sep="")