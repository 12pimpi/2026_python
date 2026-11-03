def find(array, target):
    start = 0
    end = len(array)-1

    while start <= end:
        mid =(start + end)//2
        if array[mid] == target:
            return mid
        elif array[mid]<target:
            start = mid + 1
        else:
            end = mid -1
            

arr = [1, 3, 4, 7, 8, 11, 13, 15]
result = find(arr,11)
print(f"찾는 데이터의 인덱스는:{result}")
