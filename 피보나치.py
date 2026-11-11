def seqence(n):
    if n <= 2:
        return 1
    return seqence(n-1)+seqence(n-2)



n=int(input())
a=[]
for i in range(1,n+1):
    a.append(seqence(i))
for i in range(n):
    print(a[i], end= ' ')
