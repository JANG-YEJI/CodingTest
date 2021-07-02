n, m, k = map(int, input().split())
data = list(map(int, input().split()))


data.sort(reverse=True)
answer = 0


while m:
    for i in range(k):
        answer += data[0]
        m += -1
    answer += data[1]
    m += -1

print(answer)

