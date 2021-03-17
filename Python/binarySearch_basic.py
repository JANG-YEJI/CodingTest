# Binary Search 이진 탐색: 찾으려는 데이터와 중간점 위치에 있는 데이터를 반복적으로 비교
# 이미 정렬된 데이터에서 사용 

n, target = map(int, input().split())
array = list(map(int, input().split()))

def binarySearch(array, target):
    start = 0
    end = len(array)-1
    mid = (start+end)//2

    while start <= end:
        mid = (start+end)//2

        if array[mid] == target:
            return mid+1
        elif array[mid] > target:
            end = mid-1
        else:
            start = mid+1
    return None

print(binarySearch(array, target))