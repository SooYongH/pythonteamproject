# 두 정수를 입력받아 가장 큰수를 출력
# num1 = int(input('정수1 입력 : '))
# num2 = int(input('정수2 입력 : '))
#
# if num1 >= num2 :
#     print('큰수는', num1)
# else:
#     print('큰수는', num2)

# 세 정수를 입력받아 가장 큰수를 출력
'''
num1=int(input("정수1 입력 : "))
num2=int(input("정수2 입력 : "))
num3=int(input("정수3 입력 : "))
if num1>=num2:
    max=num1
    if num1 >= num3:
        max=num1
    else:
        max=num3
elif num2 >= num3:
    max=num2
else:
    max=num3
print("제일 큰 수 :", max)

# 최윤하
if num1 > num2 and num1 > num3:
    print('가장 큰수는', num1)
elif num2> num1 and num2 > num3:
    print('가장 큰수는', num2)
else:
    print('가장 큰수는', num3)

# 강대영
if (num1 > num2) and (num1 > num3):
    print('가장 큰 수는', num1)
elif (num3 > num2) and (num3 > num1):
    print('가장 큰 수는', num3)
else:
    print('가장 큰 수는', num2)

# 김현우
a=int(input('숫자1입력:'))
b=int(input('숫자2입력:'))
c=int(input('숫자3입력:'))

if a>b:
    if a>c:
        print("가장 큰 수는 %d"%a)
    elif a==c:
        print("가장 큰 수는 %d %d"%(a,c))
    else:
        print("가장 큰 수는 %d" %c)

elif a==b:
    if a>c:
        print("가장 큰 수는 %d %d"%(a,b))
    elif a==c:
        print("가장 큰 수는 %d %d %d"%(a,b,c))
    else:
        print("가장 큰 수는 %d"%c)
else:
    if b>c:
        print("가장 큰 수는 %d"%b)
    elif b==c:
        print("가장 큰 수는 %d %d"%(b,c))
    else:
        print("가장 큰 수는 %d"%c)

# 김주연
if (a >= b) & (a >= c):
    print(f'max: {a}')
elif (b >= a) & (b >= c):
    print(f'max: {b}')
else:
    print(f'max: {c}')
'''
# 권예진
num1 = int(input('정수1 입력 : '))
num2 = int(input('정수2 입력 : '))
num3 = int(input('정수3 입력 : '))

# 이경미
if num1 > num2 and num1 > num3 :
    print('제일 큰 수는', num1)
elif num2 > num3 :
    print('제일 큰 수는', num2)
else :
    print('제일 큰 수는', num3)


# 응용 : 세 정수 중 가장 작은 수 출력