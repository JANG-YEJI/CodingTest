"""
Programmers Level2
DFS/BFS
타켓 넘버
https://programmers.co.kr/learn/courses/30/lessons/43165
https://lkhlkh23.tistory.com/74
"""

# n개의 정수를 더하거나 빼서 타켓 넘버 만들기

def solution(numbers, target):
    answer = 0

    if len(numbers) == 0:
        return 1 if target == 0  else 0
    else:
        answer = solution(numbers[1:], target+numbers[0]) + solution(numbers[1:], target-numbers[0])

    return answer


print(solution([1, 1, 1, 1, 1], 3))  #answer = 5
print(solution([2, 3, 5, 7, 9], 2))  #answer = 3