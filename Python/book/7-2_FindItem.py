n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

for i in range(m):
    if b[i] in a:
        print('yes', end=' ')
    else:
        print('no', end=' ')