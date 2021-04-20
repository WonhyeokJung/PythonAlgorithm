# Combination 1
def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return
    if idx == N:
        return

    sel[sidx] = arr[idx]
    combination(idx + 1, sidx + 1)  # 뽑고가기
    combination(idx + 1, sidx)  # 안뽑고가기


N = 5
R = 3

arr = [1, 2, 3, 4, 5]

sel = [0] * R


# Combination 2
def combination2(idx, sidx):
    if sidx == R:
        print(sel)
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i + 1, sidx + 1)


combination(0, 0)
print("-------------------------")
combination2(0, 0)


# Permutation
nums = [1, 2, 3]


def permutation(idx, length):
    if idx == length:
        print(*nums, sep=", ")

    else:
        for changer in range(idx, length):
            nums[idx], nums[changer] = nums[changer], nums[idx]
            permutation(idx+1, length)
            nums[idx], nums[changer] = nums[changer], nums[idx]

print("----------------------------")
permutation(0,3)