# https://programmers.co.kr/learn/courses/30/lessons/42583

# 트럭이 bridge_length초 만큼 다리 위에 있어야 함

def solution(bridge_length, weight, truck_weights):
    time = 0
    q = [0] * bridge_length    # 다리 위에 있는 트럭의 무게들

    while q:
        time += 1
        q.pop(0)
        if truck_weights:
            if sum(q) + truck_weights[0] <= weight:
                q.append(truck_weights.pop(0))
            else:
                q.append(0)
    return time
