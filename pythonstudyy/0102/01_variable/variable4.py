# 변수1 + 변수2 + 변수3 + ...
a, b, c, d = 10, 20, 30, 40
print(a + b + c + d) # + : 산술연산자

name = '홍길동'
address = '역삼동'
age = 20
print(name + address) # + : 연결(concatenate)연산자
print(name + '은 ' + address + "에 삽니다")
s = name + '은 ' + address + "에 삽니다"
print(s)
# print(name +'은 ' + age + '세입니다')

# + : 피연산자들이 모두 같은 데이터유형이어야 한다
# 숫자 + 숫자
# 문자열 + 문자열
print(name +'은 ' + str(age) + '세입니다')
