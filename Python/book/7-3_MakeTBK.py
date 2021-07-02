n, m = map(int, input().split())
array = list(map(int, input().split()))

start = 0
end = max(array) 
mid = (start+end)//2  

while start <= end:
    rest = 0
    for a in array:
        if a > mid:
            rest += (a-mid) 

    if rest == m:
        answer = mid
        break
    elif rest < m:
        end = mid - 1
        mid = (start+end)//2
    else:
        start = mid + 1
        answer = mid 
        mid = (start+end)//2  

print(answer)
 