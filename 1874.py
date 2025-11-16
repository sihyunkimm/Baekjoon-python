import sys

input = sys.stdin.readline

stack = []
count = 1
answer = ''

n = int(input())


def mypush():
    global count
    global answer
    global stack
    stack.append(count)
    answer += '+'
    count += 1

def mypop():
    global answer
    global stack
    temp = stack.pop()
    answer += '-'
    return temp


for _ in range(n):
    num = int(input())

    if len(stack) == 0 or stack[-1] < num:
        mypush()
        while stack[-1] < num:
            mypush()
    
    poped = mypop()

    if poped != num:
        answer = 'NO'
        break


if answer == 'NO':
    print(answer)
else:
    for i in answer:
        print(i)            