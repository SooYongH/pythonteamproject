# print() 함수의 다양한 출력
# 1. print(변수1, 변수2, ...)
# 2. format code : %d, %f, %s, %x, %o, %c
#  형식  '서식 ' % 값(변수이름)

age = 20
name = '홍길동'
address = '서초구'

print('이름은', name)
print('이름은 ' + name)
print('이름은 %s' % name)
print('나이는', age)
print('나이는 ' + str(age))
print('나이는 %d' % age)

print('이름은 %s이고  나이는 %d세입니다' % (name, age) )

# %d : 정수,  %f : 실수,  %s : 문자열,  %c : 문자

# 3. format() 함수 사용
# format(변수, 서식기호 )

print(format(age, '5d'))
print(format(name, '10s'))

# ---------------

name = '홍길동'
no = '2016001'
year = 4
grade = 'A'
average = 93.5

print('성명 :' + name)
print('학번 :' + format(no, 's'))
print('학년 :' + format(year, '5d'))
print('학점 : %s' % grade)
print('평균 :'+ format(average, '6.2f'))

format(1.234567, '10.3f')

print('### .format() 예시 ####')

# 문자열.format()함수
# 문자열 "  {} {} ".format( , )

print('성명 : {}'.format(name))
print('학번 : {}'.format(no))
print('학년 : {}'.format(year))
print('학점 : {}'.format(grade))
print('평균 : {}'.format(average))

print('학번:{1}, 성명:{0}'.format(name, no))
print('{1:3d} {0:05d} {2:.2f}'.format(123, 125, 130.456))

# print()함수의 'end='인수를 사용한 출력
print('first'); print('second')
print('first', end=''); print('second')
print('first', end=':'); print('second')

# fstring : 파이썬 3.6 이후 버전

result = f'이름은 {name}, 나이는 {age}에요'
print(result)
print(f'이름은 {name}, 나이는 {age}에요')
result2 = '이름은 {}, 나이는 {}에요'.format(name, age)
print(result2)

