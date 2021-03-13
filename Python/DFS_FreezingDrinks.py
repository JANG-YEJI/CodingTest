# N X M 크기의 얼음 틀
# 구멍이 뚫려 있는 부분 0, 칸막이 1
# 구멍이 뚫려 있는 부분끼리 상, 하, 좌, 우 붙어 있는 경우 서로 연결
# 총 생성되는 아이스크림 

# 얼음 틀의 가로 세로 길이
n, m = map(int, input().split())
# 얼음 틀의 형태
ice_f = []
for i in range(n):
    ice_f.append(list(map(int, input())))


# 특정 노드를 방문한 뒤에 연결된 모든 노드들도 방문 
def dfs(x, y):

    # 범위를 벗어나는 경우 종료
    if x <= -1 or x >=n or y <= -1 or y >= m:
        return False

    #현재 노드를 아직 방문하지 않았다면
    if ice_f[x][y] == 0:
        ice_f[x][y] = 1

        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False 

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1

print(result)
