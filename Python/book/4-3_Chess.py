start = input()

x = int(start[1])
y = int(ord(start[0]) - ord('a')) + 1

steps = [(-1, 2), (-1, -2), (1, -2), (1, 2), (-2, 1), (-2, -1), (2, 1), (2, -1)]
answer = 0

for step in steps:
    if x+step[0] > 0 and x+step[0] < 9 and y+step[1] > 0 and y+step[1] < 9:
        answer += 1

print(answer)
