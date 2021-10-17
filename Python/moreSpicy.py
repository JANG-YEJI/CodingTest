# https://programmers.co.kr/learn/courses/30/lessons/42626
# 시간초과 테케 있음

def solution(scoville, K):
    answer = 0
    
    while min(scoville) < K:
        answer += 1
        scoville.sort()
        mixed_scoville = scoville[0] + (2*scoville[1])
        
        del scoville[:2]
        scoville.append(mixed_scoville)
        
    return answer