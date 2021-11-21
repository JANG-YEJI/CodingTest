# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
# 가장 큰 수
# numbers의 원소는 0 이상 1,000 이하입니다.
# 세자리 수를 넘지 않으므로 
# str로 바꾼 뒤 3을 곱해준다

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 3, reverse=True)
    
    return str(int(''.join(numbers)))