# Distance of closest approach from Start node to each other nodes.

def dijkstra(queue):
    global dist
    if not queue:  # 큐가 비었으면 끝난것
        return
    visited.append(queue[0][0])  # 현재 시작노드
    while queue:
        arr = queue.pop(0)
        if arr[1] not in dist:  # 방문한적이 없는거죠
            if arr[0] in dist:  # 이전값이 있었다면
                dist[arr[1]] = dist[arr[0]] + arr[2]  # 이전값도 더해서 검사
            else:
                dist[arr[1]] = arr[2]  # 이전값이 없었으면 너가 최초
        elif arr[1] in dist:  # 이미 distance에 도착거리가 존재한다면 최소값 승부
            if dist[arr[0]] + arr[2] < dist[arr[1]]:  # 이전위치까지 거리 + 나까지 오는 거리 < 어디선가 나한테 온 거리
                dist[arr[1]] = dist[arr[0]] + arr[2]

    x = sorted(dist.items(), key=lambda x: x[1])  # values값 기준으로 오름차순 정렬
    for next_nord in range(len(x)):  # 최저값순이니 그 다음거로 다익스트라 돌고 break
        if x[next_nord][0] not in visited:  # 방문한적 없는 노드만
            for i in range(E):  # 그래프에서 다 넣고(현재 노드가 출발노드인 애)
                if graphs[i][0] == x[next_nord][0]:
                    queue.append(graphs[i])
            break  # 다른 노드번호에 있는건 queue에 안넣을거니까 break
    dijkstra(queue)


# (from a, to b, distance 3)
graphs = [[0,1,3], [0,2,4], [1,3,5], [2,1,1], [2,3,4], [2,4,5], [3,4,3], [3,5,4], [4,5,5]]
# graphs = [[0,1,2], [0,2,4], [1,2,1], [1,3,7], [2,4,3], [3,5,1], [4,3,2], [4,5,5]]
N = 6  # 정점개수
E = len(graphs)
dist = {0: 0, }  # 최초시작좌표, 걸린시간(당연히0). dist[i][0] = 도착노드 / dist[i][1] = 도착노드까지 걸린 최소시간
visited = []  # 이미 방문했던 노드는 최소값을 구한 상태이므로 패스.
q = []
start = 0  # i는 시작점. 시작점이 시작노드인 간선 전부 넣기.
for j in range(E):
    if graphs[j][0] == start:
        q.append(graphs[j])  #
dijkstra(q)

print(dist)




##################################################################################
# 2. Using INF
import sys


def dijkstra(queue):
    global dist
    if not queue:  # 큐가 비었으면 끝난것
        return
    visited.append(queue[0][0])  # 현재 시작노드
    while queue:
        arr = queue.pop(0)
        if dist[arr[1]] == sys.maxsize:  # 방문한적이 없는거죠
            if dist[arr[0]] != sys.maxsize:  # 이전값이 있었다면
                dist[arr[1]] = dist[arr[0]] + arr[2]
            else:
                dist[arr[1]] = arr[2]  # 이전값이 없었으면 너가 최초
        else:  # 이미 도착노드에 방문한적 있는 경우므로 최소값 승부
            if dist[arr[0]] + arr[2] < dist[arr[1]]:  # 이전위치까지 거리 + 나까지 오는 거리 < 이미 저장되어있던 최소값
                dist[arr[1]] = dist[arr[0]] + arr[2]
    x = sorted(dist.items(), key=lambda x: x[1])  # values값 기준으로 오름차순 정렬

    for next_nord in range(len(x)):  # 최저값순이니 그 다음거로 다익스트라 돌고 break
        if x[next_nord][0] not in visited:  # 방문한적 없는 노드만
            for i in range(E):  # 그래프에서 다 넣고(현재 노드가 출발노드인 애)
                if graphs[i][0] == x[next_nord][0]:
                    queue.append(graphs[i])
            break  # 다른 노드번호에 있는건 queue에 안넣을거니까 break
    dijkstra(queue)


# (from a, to b, distance 3)
sys.stdin = open("dijkstra_input.txt", "r")
for tc in range(1, int(input())+1):
    N, E = map(int, input().split())  # 정점, 간선
    graphs = [list(map(int, input().split())) for _ in range(E)]
    # 원칙적으론 dist는 각 값에 무한이 일단 할당되어있어야 한다.
    dist = {}  # 최초시작좌표, 걸린시간
    for i in range(N+1):
        dist[i] = sys.maxsize
    visited = []  # 이미 방문했던 노드는 최소값을 구한 상태이므로 패스.
    q = []
    start = 0  # 시작점. 시작점이 시작노드인 간선 전부 넣기.
    for j in range(E):
        if graphs[j][0] == start:
            q.append(graphs[j])  #
    dijkstra(q)

    print(f'#{tc} {dist[N]}')
    print(dist)