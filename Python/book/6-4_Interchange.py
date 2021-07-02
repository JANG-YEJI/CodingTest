n, k = map(int, input().split())

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort(reverse=True)


for i in range(n):
    for j in range(n):
        if a[i] < b[j]:
            tmp = a[i]
            a[i] = b[j]
            b[j] = tmp
            k += -1
            if k == 0:
                break
    if k == 0:
                break

print(sum(a))
