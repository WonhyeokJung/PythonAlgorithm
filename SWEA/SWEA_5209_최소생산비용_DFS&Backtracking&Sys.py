import sys


def backtracking(l: list, row_idx: int, idxs: list, sums: int) -> list:
    global min
    if sums > min:  # 이미 sums가 최소보다 크면 멈춰!
        return

    if row_idx == N:
        if sums <= min:
            min = sums
        return

    for idx in range(len(l)):
        if not idx in idxs:
            idxs.append(idx)
            backtracking(arr, row_idx+1, idxs, sums + l[row_idx][idx])
            idxs.pop()  # 사용한 인덱스 다시 빼줘야 안 간 것으로 체크 되니까


sys.stdin = open("5209_input.txt", "r")

for tc in range(1, int(sys.stdin.readline())+1):
    N = int(sys.stdin.readline())
    arr = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    min = 987654321

    for i in range(len(arr)):
        idxes = [i]
        backtracking(arr, 0+1, idxes, arr[0][i])

    print(f'#{tc} {min}')
