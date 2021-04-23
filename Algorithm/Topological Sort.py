# 위상정렬
# Topological sort is used for finding order in DAG.
"""
여러곳에서 시작하는 방향이 있고, 사이클 없는 그래프라면 작업순서를 출력해준다. 여러가지 답안이 가능.
조건
1. DAG(Directed acyclic graph[유향 비순환 그래프])에만 사용 가능
2. 진입차수(in-degree): Node로 들어오는 간선 개수
3. 진출차수(out-degree): Node에서 다른곳으로 나가는 간선 개수
"""

# 1. Using Queue / 242ms
"""
1. 진입차수가 0인 모든 node Queue 삽입
2. Queue가 빌 때까지 반복
    - Queue에서 원소를 꺼내 해당 v에서 나가는 간선 그래프에서 제거( = 목적지 노드의 진입차수 -1)
    - 목적지 노드 진입차수가 0이 됐다면 queue에 삽입 
3. 큐에 들어온 순서(큐에서 꺼내지는 순서) = 위상정렬 수행 결과
"""
import collections
import heapq
import sys

sys.stdin = open("../Inputs/topological_input.txt", "r")

for tc in range(1, 11):
    V, E = map(int, sys.stdin.readline().split())  # vertex, edges

    graphs = list(map(int, input().split()))
    in_degrees = collections.defaultdict(int)
    for i in range(1, V+1):  # 각자 기본 0 값으로 넣어주기
        in_degrees[i] = 0
    out_degrees = collections.defaultdict(list)  # 진출순서는 사실 상관없고, 그냥 어디로 진출하는지 담는 용도.
    for i in range(E):
        out_degrees[graphs[2*i]].append(graphs[2*i+1])
        in_degrees[graphs[2*i+1]] += 1

    queue = []
    result = []
    for i in range(len(in_degrees)):
        if in_degrees[i] == 0:
            heapq.heappush(queue, i)

    while queue:
        node = queue.pop(0)  # 앞에서부터 빼온다.
        # node = heapq.heappop(queue)  # keys가 작은 순서로 나오므로 여기선 사용 불가.

        result.append(str(node))
        for v in out_degrees[node]:
            in_degrees[v] -= 1
            if in_degrees[v] == 0:
                heapq.heappush(queue, v)

    print(f'#{tc} {" ".join(result[1:])}')


# 2. Using Stack / 244ms
"""
1. In-degree가 0인 모든 n에서 DFS 시작
2. DFS 탐색
    - 해당 node 방문 표시
    - 인접하면서 방문X node 존재시 DFS
    - return 전 현재 노드 Stack에 저장
3. 스택 공백 때까지 pop
4. Stack FILO 구조이므로 역순으로 해야 위상정렬 순서이다.
"""
import collections


sys.stdin = open("../Inputs/topological_input.txt", "r")
def topological_dfs(v):
    visited[v] = True
    for node in out_degrees[v]:
        if not visited[node]:
            topological_dfs(node)
    stack.append(str(v))  # join쓰기 위함.


for tc in range(1, 11):
    V, E = map(int, sys.stdin.readline().split())  # vertex, edges

    graphs = list(map(int, input().split()))  # 출발노드, 도착노드 순으로 간선수(E)만큼 들어온다.
    in_degrees = collections.defaultdict(int)
    for i in range(1, V + 1):  # 각자 기본 0 값으로 넣어주기
        in_degrees[i] = 0
    out_degrees = collections.defaultdict(list)  # 진출순서는 사실 상관없고, 그냥 어디로 진출하는지 담는 용도.

    for i in range(E):  # 진출차수엔 도착 노드 번호를, 진입 차수엔 들어오는 횟수만큼 +1
        out_degrees[graphs[2 * i]].append(graphs[2 * i + 1])
        in_degrees[graphs[2 * i + 1]] += 1

    visited = [False]*(V+1)
    stack = []

    for i in range(len(in_degrees)):
        if in_degrees[i] == 0:
            topological_dfs(i)

    print("#{} {}".format(tc, ' '.join(stack[1:][::-1])))  # 스택(1번째부터 끝까지, 0번 노드는 존재하지 않으므로.) 역순 출력


"""
1. 모든 정점 방문 전 Queue, Stack 공백시 사이클 존재
2. 그래프 유형은 DAG
3. O(V+E)
4. 여러 해답이 존재한다.
"""