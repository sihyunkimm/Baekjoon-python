expression = input()
stack = []
answer =''

def is_plus_minus(i):
    return (i == '+' or i == '-')

def is_multi_devide(i):
    return (i == '*' or i == '/')

# A * B / C  =  AB*C/ 
# A + B * C = ABC*+
# A * (B + C) = ABC+*
# A * (B + C + D) = ABCD++*
# (A + B) * C = AB+C*
for i in expression:
    if i.isalpha():
        answer += i

    elif is_multi_devide(i):
        if len(stack) == 0 or stack[-1] == '(':
            stack.append(i)
        elif is_multi_devide(stack[-1]):
            answer += stack.pop()
            stack.append(i)
        elif is_plus_minus(stack[-1]):
            stack.append(i)

    elif is_plus_minus(i):
        if len(stack) == 0 or stack[-1] == '(':
            stack.append(i)
        else:
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)

    elif i == '(':
        stack.append(i)

    elif i == ')':
        while stack:
            temp = stack.pop()
            if temp == '(':
                break
            else:
                answer += temp

while stack:
    answer += stack.pop()

print(answer)