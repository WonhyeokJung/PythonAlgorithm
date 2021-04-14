N = 5
R = 3

arr = [1, 2, 3, 4, 5]

sel = [0] * R


def combination(idx, sidx):
    if sidx == R:
        print(sel)
        return
    if idx == N:
        return

    sel[sidx] = arr[idx]
    combination(idx + 1, sidx + 1)  # 뽑고가기
    combination(idx + 1, sidx)  # 안뽑고가기


def combination2(idx, sidx):
    if sidx == R:
        print(sel)
        return

    for i in range(idx, N):
        sel[sidx] = arr[i]
        combination(i + 1, sidx + 1)


combination(0, 0)
