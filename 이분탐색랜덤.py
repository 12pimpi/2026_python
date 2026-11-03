import random
def find(array,target):
    start = 0
    end = len(array)-1

    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid -1

m = list(map(int, input().split()))
ran = random.choice(m)
print(f"찾고자 하는 수는 {ran}")
m.sort()
print(f"정렬된 데이터는: {m}")
result = find(m,ran)
print(f"위치는 {result}")
