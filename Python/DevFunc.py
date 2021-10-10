# https://programmers.co.kr/learn/courses/30/lessons/42586?language=python3
# math.ceil() # 올림함수

import math

def solution(progresses, speeds):
    days = []
    num = 1
    time = math.ceil((100-progresses[0])/speeds[0])
    
    for i in range(1, len(progresses)):
        if time >= math.ceil((100-progresses[i])/speeds[i]):
            num += 1
        else:
            days.append(num)
            num = 1
            time = math.ceil((100-progresses[i])/speeds[i])
    days.append(num)
    return days