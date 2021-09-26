# 크루스칼 알고리즘
# 최소한의 비용으로 신장 트리 찾기
# 신장 트리: 모든 노드를 포함하면서 사이클이 존재하지 않는 부분 그래프

# 1. 간선을 오름차순으로 정렬
# 2. 사이클이 발생할 경우 간선 포함 X
# 3. 모든 간선에 대해 2번 반복

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else: 
        parent[a] = b


v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

# 부모 테이블에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

# 간선 정보 입력받기
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost

print(result)
