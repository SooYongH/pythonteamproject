#변수와 상수 (리터럴)
# 자료형 : 숫자(정수, 실수), 문자열, 논리
# 연산자
# 조건문
# 반복문
# 문자열
# 리스트[], 튜플 (), 딕셔너리{}, 세트

#1부터 100사이의 정수 중 3의 배수의 합 출력

# for문 (조건 횟수만큼만 반복)
# total=0
# for num in range(3,101,3):
#     total+=num
# print(f'1~100사이의 3의 배수의 합은 {total}')

# while문 (만족할때까지 무한 반복)
total=0
num=3
while num<=100:
    total+=num
    num+=3
print(f'1~100사이의 3의 배수의 합은 {total}')
