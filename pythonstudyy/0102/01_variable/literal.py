# 리터럴 : 정수, 실수, 논리, None, 문자, 문자열
# 1. 정수 리터럴의 종류
# 10진수, 2진수(binary), 8진수, 16진수
a = 300
b = 0b1010
c = 0o123
d = 0xa9f

print(a, b, c, d)

# 2. 실수 리터럴
f1 = 3.14
f2 = -123.45
f3 = 12.345678
f4 = 12345634353537.3425454678786868
f5 = 123.456e7  # 10^7 => 10000000
f6 = 123.456e-7
print(f1, f2, f3, f4)
print(f5, f6)

# 문자리터럴
c1 = 'a'
c2 = 'B'
print(c1, c2)

# 문자열 리터럴
s1 = '이순신'
s2 = "python"
s3 = '''프로그래밍 
반가워용'''
s4 = """ 여러줄로
나누어 
출력해도 되어요"""
print(s1, s2)
print(s3)
print(s4)

# 5. 논리값 리터럴(참 /거짓)
b1 = True
b2 = False
print(b1, b2)

# 6. 특수 리터럴
name = '홍길동'
age = 20
address = None

print(name, age, address)

print(b, type(b))
print(f1, type(f1))
print(c1, type(c1))
print(s1, type(s1))
print(b1, type(b1))
print(address, type(address))
