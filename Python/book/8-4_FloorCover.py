# n*2바닥을 채우는 경우의 수
# 덮개: 1X2, 2X1, 2X2

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

# d[3] = d[1] * 2
# d[3] = d[2] * 1
# d[4] = d[2] * 2
# d[4] = d[3] * 1

for i in range(3, n+1):
    d[i] = (d[i-2] * 2) + (d[i-1] * 1)

result = d[n] % 796796
print(result)