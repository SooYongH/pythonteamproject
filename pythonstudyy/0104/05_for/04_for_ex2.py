# 두 정수 사이의 합계 구하기

# 이지문
# a = 'start'
# b= 'end'
# number1 = int(input(f'{a}숫자1을 입력하세요: '))
# number2 = int(input(f'{b}숫자2를 입력하세요: '))
# total = 0
# for num in range(number1,number2+1):
#     total += num
# print(f'{number1}부터 {number2}까지의 합 : {total}')

# 강대영
# total=0
# a = int(input('숫자1 입력: '))
# b = int(input('숫자2 입력: '))
# for num in range(a,b+1,1):
#     total+=num
# print(f'{a}부터 {b}까지의 합 : {total}')

# 김영민
#정수 2개를 입력 받아서 두수 사이의 합 구하기

# a = int(input())
# b = int(input())
# total=0
# for num in range(a,b+1):
#     total += num
# print(total)

#정수 2개를 입력 받아서 두수 사이의 합 구하기

# a = int(input('정수1 입력:'))
# b = int(input('정수2 입력:'))
# total=0
# for num in range(a,b+1):
#     total += num
# print(f'두 정수 사이의 합은 {total} 입니다.')

# 오유진
# num1 = int(input('숫자1 입력 : '))
# num2 = int(input('숫자2 입력 : '))
# total = 0
# for num in range(num1, num2+1):
#     total += num
# print(f'{num1}부터 {num2}까지의 합 : {total}')

# 권예진
total = 0
num1 = int(input('숫자1 입력 : '))
num2 = int(input('숫자2 입력 : '))
if num1 <= num2 :
    for nums in range(num1, num2+1) :
        total = total + nums
else :
    for nums in range(num2, num1 + 1):
        total = total + nums
print(f'{num1}부터 {num2}까지의 합 : {total}')

