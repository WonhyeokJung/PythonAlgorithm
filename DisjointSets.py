# 상호배타집합
# Basis


# Using Rank
def make_set(x):
    parents[x] = x
    rank[x] = 0
    return x


def find_set(x):
    if x != parents[x]:
        return find_set(parents[x])
    return parents[x]


def union(x, y):
    link(find_set(x), find_set(y))


def link(x, y):
    if rank[x] > rank[y]:  # x 높이가 더 높다면(자식이 더 많다.)
        parents[y] = x  # x가 부모가 됨
    else:
        parents[x] = y  # y가 부모행.
    if rank[x] == rank[y]:  # else문에선 rank[x] <= rank[y] 므로 둘의 높이 같은 경우 따로 처리.
        rank[y] += 1


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # 0~N까지의 노드개수
    arr = list(map(int, input().split()))

    parents = [0]*(N+1)  # 부모노드 번호 저장.노드개수 + 1. 0번은 비워두기
    rank = [0]*(N+1)  # 각 노드 높이 저장.

    for i in range(N+1):
        make_set(i)
    print(parents)

    for i in range(M):
        union(arr[2*i], arr[2*i+1])

    print(parents, rank)
