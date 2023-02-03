"""
# 파이썬의 키워드(예약어) 목록 확인
import keyword
keyword.kwlist
len(keyword.kwlist)


# 변수의 특징
'''
1. 변수 선언이 필요 없다
2. 다양한 자료형을 가질 수 있다.(동적타이핑: 실행할 때 자료형이 결정)
   자료형이 정해져 있지 않다.
3. 이름이 있다
4. 변수에는 다른 값을 저장할 수 있다
5. 객체가 저장되어 있는 주소 값이 저장된다.
'''
a = 1
print(a)
b = 10
print(a + b)
a = 12
print(a + b)
print(a)
print(a, b)
print(10,20)
print()

# 변수의 자료형과 메모리 주소를 확인
# 변수가 가지고 있는 데이터의 자료형 확인 : type()
# 변수의 메모리 주소를 확인 : id()

c = a+b
print(c)
a = '123'
print(a)
id(a)
type(a)
a = 100
type(a)
id(a)
a = 10.5
id(a)

# 하나의 변수에 값 저장
a = 10.5
b = 300
c = 50
d = 'hello'

# 여러 개의 변수에 여러 개의 값을 저장
x, y, z = 1, 2, 3
print(x, y, z)

# 여러 개의 변수의 한 개의 값을 저장
a = b = c = 100
print(a,b,c)

"""

# 두 변수의 값 교환
a, b = 10, 20
print(a, b)
a, b = b, a
print(a, b)

# 변수 삭제 : del 변수명
del a
print(a)
