# https://programmers.co.kr/learn/courses/30/lessons/42748
# K 번째 수

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
answer = []

len_commands = len(commands)

for n in range(len_commands):
    i = commands[n][0] -1
    j = commands[n][1]
    k = commands[n][2] -1

    slice_arr = array[i:j]
    slice_arr.sort()

    answer.append(slice_arr[k])
print(answer)



def solution(array, commands):

    answer = []

    len_commands = len(commands)

    for n in range(len_commands):
        i = commands[n][0] -1
        j = commands[n][1]
        k = commands[n][2] -1

        slice_arr = array[i:j]
        slice_arr.sort()

        answer.append(slice_arr[k])
        
    return answer