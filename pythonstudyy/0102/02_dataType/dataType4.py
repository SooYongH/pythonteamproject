# 두 개의 정수를 입력받고 합계와 평균 구하기

num1 = int(input('숫자1: '))
num2 = float(input('숫자2: '))
print(num1, num2)
print(type(num1))
print(type(num2))
total = num1 + num2
avg = total/2
# print(int(num1) + int(num2))
# print((int(num1) + int(num2))/2)
print(f'합계는 {total}, 평균은 {avg:.3f}')

# eval() 함수

# num1 = eval(input('숫자1: '))
# num2 = eval(input('숫자2: '))
# print(num1, num2)
# print(type(num1))
# print(type(num2))