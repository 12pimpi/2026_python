def countdown(n):
    if n==0:
        print("끝!!")
        return
    print(n)
    countdown(n-1)

countdown(4)
