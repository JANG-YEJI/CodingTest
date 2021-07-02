n, m = map(int, input().split())
x, y, d = map(int, input().split())

array  = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 방문 유무
visit = [[0] * m for _ in range(n)]
visit[x][y] = 1

# 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

while True:
    for i in range(4):
        if d-1 < 0:
            d = 3
        else:
            d = d-1

        nx = x + dx[d]
        ny = y + dy[d]

        if visit[nx][ny] == 0 and array[nx][ny] == 0:
            x = x + dx[d]
            y = y + dy[d]
            visit[x][y] = 1
            break

    x = x + 1
    y = y
    visit[x][y] = 1

    if array[x][y] == 1:
        visit[x][y] = 0
        break

answer = 0
for i in range(n):
    for j in range(m):
        answer += visit[i][j]
        

print(answer)




