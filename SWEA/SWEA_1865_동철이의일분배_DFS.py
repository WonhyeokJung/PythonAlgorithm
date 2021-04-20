# append, pop 사용. 9787ms
def backtracking(l: list, row_idx: int, idxs: list, sums: int) -> list:
    global maxs
    if maxs >= sums:
        return
    if row_idx == N:
        if sums > maxs:
            maxs = sums
        return

    for idx in range(len(l)):
        if not idx in idxs and l[row_idx][idx] != 0:
            idxs.append(idx)
            backtracking(l, row_idx + 1, idxs, sums * l[row_idx][idx] / 100)
            idxs.pop()  # 사용한 인덱스 다시 빼줘야 안 간 것으로 체크 되니까


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxs = 0

    for i in range(len(arr)):
        if arr[0][i] != 0:
            backtracking(arr, 0 + 1, [i], arr[0][i] / 100)

    maxs *= 100
    print(f'#{tc} {"%.6f" % maxs}')


print("##########################")


# 2. visited[n] 사용. 5071ms
def backtracking(l: list, row_idx: int, sums: int) -> list:
    global maxs
    if maxs >= sums:
        return
    if row_idx == N:
        if sums > maxs:
            maxs = sums
        return

    for idx in range(len(l)):
        if visited[idx] == 0:
            visited[idx] = 1
            backtracking(l, row_idx + 1, sums * l[row_idx][idx] / 100)
            visited[idx] = 0


for tc in range(1, int(input()) + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    maxs = 0
    visited = [0] * N

    for i in range(len(arr)):
        visited[i] = 1
        backtracking(arr, 0 + 1, arr[0][i] / 100)
        visited[i] = 0

    maxs *= 100
    print(f'#{tc}', end = ' ')
    print(format(maxs, '.6f'))
    print("#{} {}".format(tc, "%.6f" % maxs))



