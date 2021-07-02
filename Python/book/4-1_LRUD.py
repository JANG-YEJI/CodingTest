n = int(input())
plans = list(input().split())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L', 'R', 'U', 'D']

x = 1
y = 1

for plan in plans:
    i = move_types.index(plan)

    if x+dx[i] > 0 and y+dy[i] > 0 and x+dx[i] <= n and y+dy[i] <= n:
        x += dx[i]
        y += dy[i]

print(x, y)
