# 위상 정렬
# 순서가 정해져 있는 작업을 차례대로 수행 

# 1. 진입차수가 0인 노드를 큐에 넣는다.
# 2. 큐가 빌 때까지 다음의 과정을 반복한다.
# 2-1. 큐에서 원소를 꺼내 해당 노드에서 출발하는 간선을 그래프에서 제거한다
# 2-2. 새롭게 진입차수가 0이 된 노드를 큐에 넣는다. 

# 모든 원소를 방문하기 전에 큐가 빈다면 사이클이 발생
# 대부분 사이클이 발생하지 않는다고 명시되어진 문제가 많음

from collections import deque

v, e = map(int, input().split())
indegree = [0] * (v+1)
graph = [[] for i in range(v+1)]

# 간선 정보 입력
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b) # 정점 A에서 B로 이동 가능
    indegree[b] += 1 # 진입 차수를 1 증가

#위상 정렬 합수
def topology_sort():
    result = []
    q = deque()

    # 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        result.append(now)
        for i in graph[now]:
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    for i in result:
        print(i, end=' ')

topology_sort()