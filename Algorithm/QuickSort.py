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
def quicksort(arr,l,r):
    # if l >= r:
    #     return
    if l < r:
        mid = partition(l,r)
        quicksort(arr, l, mid-1)
        quicksort(arr, mid+1, r)

def partition(l,r):
        p = l
        pivot = array[l]
        while l <= r:
            while l <= r and array[l] <= pivot:
                l += 1
            while l <= r and array[r] >= pivot:
                r -= 1
            if l < r:
                array[l], array[r] = array[r], array[l]

        array[p], array[r] = array[r], array[p]
        return r


print(quicksort(array, 0, len(array)-1))
print(array)

