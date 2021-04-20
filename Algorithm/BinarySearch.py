# 정렬된 list의 middle index를 찾아서, 그 값보다 크면 우측을 그 값보다 작으면 좌측을 탐색하는 방식.
# 1. recursive
def binarySearch2(arr, low, high, key):
    if low > high : # 검색실패
        return False
    else :
        middle = (low + high) // 2
        if key == arr[middle]: # 검색 성공
            return True
        elif key < arr[middle]:
            return binarySearch2(arr, low, middle-1, key)
        elif arr[middle] < key:
            return binarySearch2(arr, middle+1, high, key)


# 2.
def binarySearch(arr, key):
    start = 0
    end = len(arr)-1
    while start <= end:
        middle = (start + end)//2
        if arr[middle] == key: # 검색 성공
            return True
        elif arr[middle] > key:  # 찾는 값이 arr[middle]보다 작으면 좌측 탐색
            end = middle - 1
        elif arr[middle] < key:
            start = middle + 1
    return False  # 검색 실패