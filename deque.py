from collections import deque

n = int(input())
q = deque()
for _ in range(n):
    command = input().split()
    if command[0] =='a':
        q.append(int(command[1]))
    elif command[0] == 'p':
        if len(q) == 0:
            print("empty")
        else:
            print(q.popleft())
    elif command[0] == 'l':
        print(len(q))