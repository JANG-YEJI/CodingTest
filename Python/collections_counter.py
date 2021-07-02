from collections import Counter

# 중복 제거
participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]

answer = Counter(participant) - Counter(completion)
print(Counter(participant))
print(answer)