"""

O(nlogn) / Worst : O(n**2)
주어진 배열을 기준아이템(Pivot Item) 중심으로 작은 수들 / 큰 수들로 분할 후, 각각을 정렬

"""

# 1. Romuto Partition
array = [69, 10, 30, 2, 16, 8, 31, 22]


# def quicksort(a, begin, end) :
#     def partition(begin, end):
#         pivot = a[end]  # 배열의 마지막 항
#         left = begin
#         for right in range(begin, end):
#             if a[right] < pivot:
#                 a[left], a[right] = a[right], a[left]
#                 left += 1
#         a[left], a[end] = a[end], a[left]
#         return left
#     if begin < end:
#         pivot = partition(begin, end)
#         quicksort(a, begin, pivot - 1)  # 피벗 왼쪽
#         quicksort(a, pivot + 1, end)  # pivot 오른쪽
#     return a
#
#
# print(f'1. Romuto Partition : {quicksort(array, 0, 7)}')
# array = [69, 10, 30, 2, 16, 8, 31, 22]


# 2. Hoare Partition
def quicksort(arr, start, end):
    if start < end:
        pivot = partition(arr, start, end)
        print(pivot, start, end)
        quicksort(arr, start, pivot-1)
        quicksort(arr, pivot+1, end)
    return arr


def partition(arr, left, right):
    pivot = arr[left]
    left = left + 1  # pivot 바로 다음거
    right = right

    while left < right:
        if arr[left] > pivot:  # arr[L]이 pivot보다 크면 arr[R]값이 pivot보다 작을때까지 이동
            while left <= right and arr[left] > arr[right]:
                right -= 1
            arr[left], arr[right] = arr[right], arr[left]
        left += 1
    # left & right 값이 교차되었음.
    arr[left], arr[right] = arr[right], arr[left]
    print(arr)
    return right  # new pivot index


print(quicksort(array, 0, len(array)-1))
print(array)

