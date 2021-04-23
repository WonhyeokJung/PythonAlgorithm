# Distance of closest approach from Start node to each other nodes.
# 특정지점부터 다른 지점까지 가는 최소의 거리, 다익스트라 알고리즘.
import heapq
import collections
import sys


def dijkstra(Q, graph):
    # maxsize = sys.maxsize
    maxsize = 987654321
    for _ in range(1, N + 1):  # 출발점별 최소거리 계산
        distance = [maxsize] * (N + 1)  # 새로 큐 돌때마다 distance 초기화해서 재체크
    while Q:
        times, node = heapq.heappop(Q)
        if times < distance[node]:
            distance[node] = times
            for v, w in graph[node]:  # 도착지, 시간
                heapq.heappush(Q, (times+w, v))

    return distance


# (from a, to b, distance 3)
sys.stdin = open("../Inputs/dijkstra_input.txt", "r")
for tc in range(1, int(input())+1):
    N, E, X = map(int, input().split())  # 정점수, 간선수, 출발지
    graphs = collections.defaultdict(list)  # 인접행렬, 인접리스트 사용해도 괜찮음.

    for _ in range(E):
        u, v, w = map(int, input().split())
        graphs[u].append((v, w))

    queue = []
    # 도착지에서 출발 구하기
    queue.append((0, X))  # 거리, 출발노드 ( distance is 0 to reach myself )

    print(f'#{tc} {dijkstra(queue, graphs)[1:]}')  # there is no node "0" in this input