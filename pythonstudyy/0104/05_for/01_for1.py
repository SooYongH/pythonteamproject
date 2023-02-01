# for문 형식
# for 변수 in 리스트(튜플) 또는 범위 :
#     반복문장1
#     반복문장2
#     ...
# 기본자료형 : 숫자(정수, 실수), 문자, 문자열, 논리값
# 리스트 : ['banana', 'apple', 'coconut', 'melon']
# 예1.
# for name in ['banana', 'apple', 'coconut', 'melon']:
#     print(name)
#
# for num in [0,1,2,3,4,5,6,7,8,9]:
#     print(num)
#
# nums = [0,1,2,3,4,5,6,7,8,9]
# for num in nums:
#     print(num, end=' ')

# for num in range(10):
#     print(num)

# range()함수
# range(stop) : 0 ~ stop-1까지의 정수
#   => range(start=0, stop, step=1)
# range(start, stop) : start ~ stop-1까지의 정수
# range(start, stop, step) : start ~ stop-1까지의 정수 중 step간격씩 커지는 수
# range(5) == range(0, 5, 1)
# range(3, 20) == range(3, 20, 1)
# range(10, 1)  == range(10, 1, 1) 수행안됨

# print(list(range(10)))
# print(list(range(1, 10)))
# print(list(range(3, 20, 2)))
#
# for num in range(1, 10):
#     print(num, end=' ')
# print()
for num in range(1, 10, 3):
    print(num, end=' ')
#
print()
# for num in range(10, 1, -1):
#     print(num, end=' ')

# 예. 11~20사이의 정수 출력
for num in range(11,21):
    print(num)

# 예. 1~10사이의 정수 중 홀수만 출력
for num in range(1,10,2):
    print(num, end=' ')

print()

# 예. 1~10사이의 정수 중 짝수만 출력
for num in range(2, 11, 2):
    print(num, end=' ')

print()

# Tip. for문에서 반복을 위해 지정한 변수이름을 사용하지 않는 경우
# 변수이름 대신 _(underscore)를 지정하여 사용
for i in range(5):
    print('Welcome!')

for _ in range(5):
    print('Welcome!')