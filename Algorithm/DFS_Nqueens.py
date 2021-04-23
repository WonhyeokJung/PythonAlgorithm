# input : Test case, chess maps size(N = N*N)
import sys
sys.stdin = open("../Inputs/nqueen_input.txt", "r")


def DFS(arr: list, y: int, x: int):  # arr = chess map, y = row, x = column
    global cnt
    arr[y][x] = 1  # 자기자신
    dy = [-1, -1, 0, 1, 1, 1, 0, -1]
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    for j in range(8):
        new_y = y + dy[j]
        new_x = x + dx[j]
        while 0 <= new_y < len(arr) and 0 <= new_x < len(arr):  # 좌우 대각선 탐색
            if arr[new_y][new_x] == 1:
                return
            new_y += dy[j]
            new_x += dx[j]

    if y == N-1:  # 전부 검증 끝난경우
        cnt += 1
        return

    for k in range(len(arr)):
        DFS(arr, y+1, k)
        arr[y+1][k] = 0


for tc in range(1, int(input())+1):
    N = int(input())
    chess_maps = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        DFS(chess_maps, 0, i)  # chess_maps[0][i]
        chess_maps[0][i] = 0
    print("#{} {}".format(tc, cnt))