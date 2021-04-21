# This is not completed one. still working on this.
# 내가 있는 곳으로 오는 node들을 검토하는 방식을 추구해야 함.

def dijkstra(queue):
    global dist
    while queue:
        arr = queue.pop(0)
        if arr[1] not in dist:
            if arr[0] in dist:  # 이전값이 있었다면
                dist[arr[1]] = dist[arr[0]] + arr[2]  # 이전값도 더해서 검사
            else:
                dist[arr[1]] = arr[2]  # 이전값이 없었으면 너가 최초
        elif arr[1] in dist:  # 이미 distance에 도착거리가 존재한다면 최소값 승부
            if dist[arr[0]] + arr[2] < dist[arr[1]]:  # 이전위치까지 거리 + 나까지 오는 거리 < 어디선가 나한테 온 거리
                dist[arr[1]] = dist[arr[0]] + arr[2]



# (from a, to b, distance 3)
graphs = [[0,1,3], [0,2,4], [1,3,5], [2,1,1], [2,3,4], [2,4,5], [3,4,3], [3,5,4], [4,5,5]]
graphs = [[0,1,2], [0,2,4], [1,2,1], [1,3,7], [2,4,3], [3,5,1], [4,3,2], [4,5,5]]
N = 6
E = len(graphs)
q = []
dist = {0:0}
i = 0
while i < N:
    for j in range(E):
        if graphs[j][0] == i:
            q.append(graphs[j])
    dijkstra(q)
    i += 1
print(dist)