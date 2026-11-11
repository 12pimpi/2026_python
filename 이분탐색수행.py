import random

nums = list(map(int,input("임의의 수를 입력해주세요 : ").split()))
target = random.choice(nums)

nums.sort()
print(f"정렬된 배열 : {nums}")
print(f"목표 수 : {target}")

def find(array, target):
    start = 0
    end = len(array) - 1
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] < target:
            start = mid + 1
        else:
            end = mid - 1

result = find(nums, target)
print(f"인덱스 : {result}")
