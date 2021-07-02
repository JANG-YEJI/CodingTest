n, m = map(int, input().split())
max = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    if min_value > max:
        max = min_value

print(max)

