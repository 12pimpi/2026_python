token=input().split()
stack=[]

for i in reversed(token):
    if i in ('+','-','*','/'):
        b = stack.pop()
        a = stack.pop()

        if i == '+':
            stack.append(a+b)
        elif i == '-':
            stack.append(a-b)
        elif i == '*':
            stack.append(a*b)
        else:
            stack.append(a//b)
    else:
        stack.append(int(i))
print(stack[0])
