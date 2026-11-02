def space(s):
    p = -1
    count = 0
    for i in range(len(s)):
        if s[i] == ' ':
           count += 1
           if p == -1:
               p = i
    return p, count



s = input()
p, count = space(s)
print(f"첫 번째 공백의 위치는 {p}, 공백의 개수는 {count}")
