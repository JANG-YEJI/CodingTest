# https://programmers.co.kr/learn/courses/30/lessons/42587

def solution(priorities, location):
    loc = [i for i in range(len(priorities))]
    # 해당 index가 인쇄되는 순서 
    loc_prior = []
    
    while priorities:
        if priorities[0] == max(priorities):
            loc_prior.append(loc.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
            
    return loc_prior.index(location) + 1
            
