# DFS 깊이 우선 탐색

#그래프 표현 방식 2가지: Adjacency Matrix, Adjacency List
#Adjacency Matrix 
#노드 1, 2, 3  
#간선 7(0, 1), 5(0, 2)
INF = 999999999
adj_matrix = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]
print("adj_matrix: " , adj_matrix)


#Adjacency List 
#행이 3개인 2차원 리스트로 인접 리스트 표현
adj_list = [[] for _ in range(3)]
#노드 0에 연결된 노드 정보 저장(노드, 거리)
adj_list[0].append((1, 7))
adj_list[0].append((2, 5))
#노드 1
adj_list[1].append((0, 7))
#노드2
adj_list[2].append((0,5))
print("adj_list: " , adj_list)

######## 인접 행렬 -> 모든 관계 저장, 인접 리스트 -> 연결된 정보만 저장
######## 메모리 효율: 인접 리스트 > 인접 행렬
######## 속도: 인접 행렬 > 인접 리스트 (특정한 두 노드가 연결되어 있는지 확인할 때)


# DFS 동작 과정
# 1. 시작 노드를 스택에 삽입하고 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접 노드가 있으면, 
# 그 인접 노드를 스택에 넣고 방문처리 한다.
# 방문하지 않은 인접 노드가 없으면 스택에서 최상단 노드를 꺼낸다.
# 3. 2번 과정을 더이상 수행할 수 없을 때 까지 반복

def dfs(graph, v, visited):
    #현재 노드를 방문 처리
    visited[v] = True
    print(v, end = ' ')
    #현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9
dfs(graph, 1, visited)