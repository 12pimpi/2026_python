n = int(input())
stack = []

for _ in range(n):
    command = input().split()
    if command[0] == 'a':
        stack.append(command[1])
    elif command[0] == 'p':
        if len(stack) == 0:
            print('empty')
        else:
            print(stack.pop())
    elif command[0] == 'l':
        print(len(q))
