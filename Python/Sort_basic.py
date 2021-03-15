# Selection Sort 선택 정렬: 가장 작은 것을 선택하여 앞으로
# Insertion Sort 삽입 정렬: 데이터를 하나씩 확인하며 적절한 위치에 삽입
# Quick Sort 퀵 정렬: 기준 데이터를 설정하고 기준보다 큰 데이터와 작은 데이터의 위치를 바꾼다

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selectionSort(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]

    return array


def insertSort1(array):
    for i in range(len(array)):
        for j in range(0, i):
            if array[i] < array[j]:
                array = array[:i-1] + array[j] + array[i:]

    return array

def insertSort2(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    return array    


def quickSort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quickSort(left_side) + [pivot] + quickSort(right_side)