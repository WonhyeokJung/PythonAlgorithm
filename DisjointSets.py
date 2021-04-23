# 상호배타집합
# Basis
import sys

# Using Rank
def make_set(x):
    parents[x] = x
    rank[x] = 0


def find_set(x):
    if x != parents[x]:
        find_set(parents[x])
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


N = 0
parents = [0]*(N+1)  # 부모노드 번호 저장.노드개수 + 1. 0번은 비워두기
rank = [0]*(N+1)  # 각 노드 높이 저장.

for i in range(N+1):
    make_set(i)


#################################################################
# No Rank ver.
sys.stdin = open("Inputs/DisjointSets_basis_input.txt", "r")
def make_set(x):
    parents[x] = x
    return x


def find_set(x):
    if x != parents[x]:
        return find_set(parents[x])
    return x


def union(x, y):
    parents[find_set(y)] = find_set(x)  # x의 부모가 y의 부모


for tc in range(1, int(input())+1):
    N, M = map(int, input().split())  # 0~N까지의 노드개수
    arr = list(map(int, input().split()))

    parents = [0]*(N+1)  # 부모노드 번호 저장.노드개수 + 1. 0번은 비워두기
    rank = [0]*(N+1)  # 각 노드 높이 저장.

    for i in range(N+1):
        make_set(i)

    for i in range(M):
        union(arr[2*i], arr[2*i+1])

    # 각자 최고 부모 찾기
    for i in range(len(parents)):
        parents[i] = find_set(i)
    print("#{} {}".format(tc, len(set(parents[1:]))))  # 맨앞의 0빼기


##########################################
# KRUSUKAL
"""
0. 정점 개수가 V라면, 간선 개수는 V-1개가 MST
1. 간선을 오름차순으로 정렬(가중치 기준으로)
2. 가중치가 가장 작은걸 갖고있는 노드에서 시작 or 정해진 노드가 있다면 거기서 시작
3. ans += 그 가중치
4. 다음 가중치 작은 간선에서 연결 시도 후 ans += 
5. 매 간선마다 두 노드중 작은 노드가 부모노드로.
"""
print("###################################### Krusukal ########################################")
sys.stdin = open("Inputs/DisjointSets_KRUSUKAL_input.txt", "r")

def make_set(x):
    parents[x] = x


# 경로 압축
def find_set(x):
    if parents[x] != x:
        parents[x] = find_set(parents[x])
    return parents[x]


def union(x, y):
    parents[find_set(y)] = find_set(x)


for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    # 간선 입력
    edges = [list(map(int, input().split())) for _ in range(E)]

    # 크루스칼을 하기 위해서 간선을 가중치 순으로 오름차순 정렬
    edges = sorted(edges, key=lambda x: x[2])

    parents = [0] * (V+1)

    for i in range(V+1):
        make_set(i)

    ans = 0
    cnt = 0  # 간선 선택 회수
    idx = 0  # 간선의 인덱스

    while cnt < V:  # 간선수가 V-1개까지므로.
        x = edges[idx][0]
        y = edges[idx][1]

        if find_set(x) != find_set(y):
            union(x, y)
            cnt += 1
            ans += edges[idx][2]
        idx += 1
    print("#{} {}".format(tc, ans))



#############################################################
# Prim

sys.stdin = open("Inputs/DisjointSets_Prim_input.txt")
def Prim():
    global ans

    dist = [sys.maxsize]*(V+1)
    visited = [False]*(V+1)

    dist[V] = 0
    for _ in range(V):
        min_idx = -1
        min_value = sys.maxsize

        for i in range(V+1):
            if not visited[i] and dist[i] < min_value:
                min_idx = i
                min_value = dist[i]
        visited[min_idx] = True

        # 갱신할 수 있으면 갱신하자
        for i in range(V+1):
            if not visited[i] and adj[min_idx][i] < dist[i]:
                dist[i] = adj[min_idx][i]

    return sum(dist)



print("######################################Prim########################################")
for tc in range(1, int(input())+1):
    V, E = map(int, input().split())

    adj = [[sys.maxsize]*(V+1) for _ in range(V+1)]

    # 인접행렬
    for i in range(E):
        st, ed, w = map(int, input().split())
        adj[st][ed] = adj[ed][st] = w
    print("#{} {}".format(tc, Prim()))
