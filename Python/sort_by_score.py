# 성적이 낮은 순서로 학생 이름 출력하기

# 학생 수 
n = int(input())
# 이름 + 점수 입력 예) 홍길동 95
array = []
for i in range(n):
    input_data = input().split()
    array.append((input_data[0], int(input_data[1])))

# 정렬
# key parameter: 정렬을 목적으로 하는 함수를 값으로 넣는다.
array = sorted(array, key = lambda x: x[1])

for x in array:
    print(x[0], end=' ')