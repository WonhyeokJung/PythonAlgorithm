"""
5 6
1 2 1 3 3 2 3 4 2 5 5 4
"""

V, E = map(int, input().split())  # 정점(vertex, node), 간선수
edge = list(map(int, input().split()))  # 간선 리스트
# if there is not Edge enough, use memory too much
adj = [[0]*(V+1) for _ in range(V+1)]  # 인접행렬 adjacent array
# need to check all if you want to check n1 and n2 are connected
adjList = [[] for _ in range(V+1)]  # 인접리스트 adjacent list

for i in range(E):
    n1 = edge[i*2]
    n2 = edge[i*2+1]
    adj[n1][n2] = 1
    adj[n2][n1] = 1  # 무향 그래프인 경우 대칭

    adjList[n1].append(n2)
    adjList[n2].append(n1)  # 무향인 경우

print(adj, adjList)


# 1.BFS using Queue
def BFS(s, V):  # 시작점 s, 정점 개수 V
    Queue = [s]
    visited = [0]*(V+1)
    visited[s] = 1
    while Queue:
        t = Queue.pop(0)  # FIFO
        print(t)  # visit(t), do(t)
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                Queue.append(i)
                visited[i] = 1


BFS(1, V)

# 2.BFS way to reach the goal as minimum depth
def BFS2(s, V):  # 시작점 s, 정점 개수 V
    Queue = [s]
    visited = [0]*(V+1)
    visited[s] = 1
    while Queue:
        t = Queue.pop(0)  # FIFO
        print(t)  # visit(t), do(t)
        for i in range(1, V+1):
            if adj[t][i] == 1 and visited[i] == 0:
                Queue.append(i)
                visited[i] = visited[t] + 1  # 출발한 노드 값을 더함. 최소거리 정보 출력 가능

    print(visited)


BFS2(1, V)


# 3.DFS recursive
print("DFS recursive")
def DFS(s):  # nodes num
    visited[s] = 1
    print(s)
    for i in range(len(adjList[s])):
        if adjList[s][i] and not visited[adjList[s][i]]:
            DFS(adjList[s][i])
            # visited[s] = 0  # 돌아가면 다시 다른 길들도 찾게 하고 싶은 경우.


visited = [0]*(V+1)
DFS(1)


# 4. DFS using stack