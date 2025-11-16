import sys

temp = sys.stdin.readline().rstrip()

while temp != ".":
    stack = []
    for l in temp:
        if l == "(" or l == "[":
            stack.append(l)
        elif l == ")":
            if len(stack) > 0 and stack[-1] == "(":
                stack.pop()
            else:
                print("no")
                break
        elif l == "]":
            if len(stack) > 0 and stack[-1] == "[":
                stack.pop()
            else:
                print("no")
                break 
        else:
            pass
    else:
        if len(stack) != 0:
            print("no")
        else:
            print("yes")

    temp = sys.stdin.readline().rstrip()
