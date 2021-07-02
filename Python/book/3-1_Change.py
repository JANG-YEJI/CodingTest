coins = [500, 100, 50, 10]

N = int(input())
remain = N
answer = 0

for c in coins:
    answer += remain//c
    remain = remain%c

print(answer)