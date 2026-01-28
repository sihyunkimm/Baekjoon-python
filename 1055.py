import sys

MAX = 31

firstStr = input()
inputStr = input()
repeat = int(input())
start, finish = map(int, input().split())

# cache[i] = i번 반복했을 때 길이
cache = [0] * MAX  # 2^30 = 1,073,741,824
found = False
result = []
def searchChar(level, idx):
    global found, result
    pos = 0
    i = 0
    
    while not found and i < len(inputStr):
        if inputStr[i] == '$':
            # 반복 횟수 기준으로 나눔
            if level == 1:
                if idx <= pos + cache[level] - 1:
                    found = True
                    result.append(firstStr[idx - pos])
                else:
                    pos += cache[level]
            elif level > 1:
                if idx <= pos + cache[level] - 1:
                    searchChar(level-1, idx-pos)
                else:
                    pos += cache[level]
        else:
            if pos == idx:
                found = True
                result.append(inputStr[i])
                return
            else:
                pos += 1
        i += 1
   
dollar = 0
nonDollar = 0
for i in range(len(inputStr)):
    if inputStr[i] == '$':
        dollar += 1
    else:
        nonDollar += 1

# $가 하나이면 길이가 천천히 증가하여 따로 처리
if dollar < 2:
    for i in range(start - 1, finish):
        if i < len(firstStr):
            result.append(firstStr[i])
        elif i >= len(firstStr) + (len(inputStr) - 1) * repeat:
            result.append("-")
        else:
            result.append(inputStr[(i - len(firstStr)) % (len(inputStr) - 1) + 1])
    print(''.join(result))

# $가 2개부터이면 지수 비례하여 증가하므로 도중에 중단 가능
else:
    cache[1] = len(firstStr)
    for i in range(2, repeat + 1):
        cache[i] = cache[i - 1] * dollar + nonDollar
        if cache[i] > finish:
            repeat = i
            break
    
    for i in range(start - 1, finish):
        temp = repeat        
        if i >= cache[temp] * dollar + nonDollar:
            result.append("-")
            continue
        
        while temp > 1 and cache[temp] > i:
            temp -= 1
        
        found = False
        searchChar(temp, i)
    
    print(''.join(result))





# import sys
# sys.setrecursionlimit(10**5)

# firstStr = input()
# sList = list(input())
# repeatNum = int(input())
# startNum, endNum = map(int, input().split())

# sTokenList = []
# temp = ""
# dollarCnt = 0
# for c in sList:
#     if c == '$':
#         sTokenList.append(c)
#         dollarCnt += 1
#     elif c != '$' and sTokenList[-1] == "$":
#         sTokenList.append(c)
#     else:
#         sTokenList[-1] += c

# charCnt = 0
# def recur(stack):
#     global repeatNum
#     global charCnt
#     if stack >= repeatNum:
#         for token in sTokenList:
#             if token == '$':
#                 if charCnt + len(firstStr) < startNum:
#                     pass
#                 elif charCnt < startNum <= charCnt+len(firstStr):
#                     if charCnt+len(firstStr) <= endNum:
#                         print(firstStr[startNum-charCnt-1:], end='')
#                     else:
#                         print(firstStr[startNum-charCnt-1:endNum-charCnt], end='')
#                         exit(0)
#                 else:
#                     if charCnt+len(firstStr) <= endNum:
#                         print(firstStr, end='')
#                     else:
#                         print(firstStr[:endNum-charCnt], end='')
#                         exit(0)
#                 charCnt += len(firstStr)

#             else:
#                 if charCnt + len(token) < startNum:
#                     pass
#                 elif charCnt < startNum <= charCnt+len(token):
#                     if charCnt+len(token) <= endNum:
#                         print(token[startNum-charCnt-1:], end='')
#                     else:
#                         print(token[startNum-charCnt-1:endNum-charCnt], end='')
#                         exit(0)
#                 else:
#                     if charCnt+len(token) <= endNum:
#                         print(token, end='')
#                     else:
#                         print(token[:endNum-charCnt], end='')
#                         exit(0)
#                 charCnt += len(token)

#         return


#     for token in sTokenList:
#         if token == '$':
#             recur(stack+1)

#         else:
#             if charCnt + len(token) < startNum:
#                 pass
#             elif charCnt < startNum <= charCnt+len(token):
#                 if charCnt+len(token) <= endNum:
#                     print(token[startNum-charCnt-1:], end='')
#                 else:
#                     print(token[startNum-charCnt-1:endNum-charCnt], end='')
#                     exit(0)
#             else:
#                 if charCnt+len(token) <= endNum:
#                     print(token, end='')
#                 else:
#                     print(token[:endNum-charCnt], end='')
#                     exit(0)
#             charCnt += len(token)


# recur(1)
# if charCnt < endNum:
#     print('-'*(endNum-charCnt))
