# 일직선상에 존재하는 식량창고 약탈
# 최소한 한 칸 이상 떨어진 식량창고를 약탙
# 최대한 많은 식량을 얻기

n = int(input())
k = list(map(int, input().split()))

d = [0] * n

d[0] = k[0]
d[1] = max(k[0], k[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + k[i])

print(d[n-1])