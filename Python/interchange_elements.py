# 두 배열의 원소 교체
# 배열 A의 모든 원소의 합이 최대가 되도록 한다

# n: 배열 크기, k: 최대 k번 바꿔치기
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)

for i in range(n):
    if k == 0:
        break
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
        k -= 1
    else:
        break

print(sum(a))