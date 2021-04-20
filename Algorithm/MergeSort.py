# 리스트를 각각 하나씩으로 최대 분할
def divine(a:list):
    if len(a) == 1:
        return a
    left = []
    right = []
    middle = len(a)//2
    for i in range(0, middle):
        left.append(a[i])
    for i in range(middle, len(a)):
        right.append(a[i])

    # list가 len이 1이 될때까지 재귀, length 1 짜리 list a를 merge에 return
    # 왼쪽으로 계속가서 맨왼쪽 합병, 그 다음 그 옆에꺼 합병 후 이 둘을 다시 merge후 왼쪽에 저장
    return merge(divine(left), divine(right))


def merge(left:list, right:list) ->list:
    result = []

    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        elif len(left) > 0:
            result.append(left.pop(0))
        elif len(right) > 0:
            result.append(right.pop(0))

    return result


# 아래 주어지는 리스트를 Merge Sort 하시오.
sample = [69, 10, 30, 2, 16, 8, 31, 22]

print(divine(sample))

# 2. Way not to use pop()
def divine(a: list):
    if len(a) == 1:
        return a
    middle = len(a) // 2
    return merge(divine(a[:middle]), divine(a[middle:]))


def merge(left: list, right: list) -> list:
    result = []

    i = 0
    j = 0
    while i < len(left) or j < len(right):
        if i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        elif i < len(left):
            result.append(left[i])
            i += 1
        elif j < len(right):
            result.append(right[j])
            j += 1

    return result