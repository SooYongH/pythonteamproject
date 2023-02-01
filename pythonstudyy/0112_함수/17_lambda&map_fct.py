# 람다(lambda) 함수
# - 값을 반환하기 위해 return문을 사용하지 않는다
# - 람다 함수의 몸체는 문이 하나인 식의 형태
# 이름이 없는 한줄 함수

# 람다 표현식
# 형식1.  lambda : 반환할 식

# labmda: 1
# <function <lambda> at 0x000001D893C5EA20>

f = lambda : 1
print(f())

# 형식2.  lambda 인수들 : 반환할 식
add = lambda x, y : x+y
print(add(10, 20))

# def add(x,y):
#     return x+y
# print(add(10,20))

# 디폴트 인수 사용
add2 = lambda x=10, y=10 : x+y
print(add2())
print(add2(5))
print(add2(5, 500))

# 형식3. (lambda 매개변수들: 식)(인수들)
#  : 람다 표현식을 변수에 할당하지 않고 그 자체를 호출
print((lambda x : x+10)(100))

# 람다 표현식 안에서는 변수를 생성할 수 없다
# print((lambda x : y=5; x+y )(100))
# SyntaxError: invalid syntax

def plus(x):
    y=5
    return x+y

def plus2(x, y):
    return x+y

# 람다표현식 바깥에 있는 변수 사용 가능
y=5
print((lambda x : x+y )(100))

# 문제. plus_ten(x)과 같은 기능을 하는 람다표현식 정의
# def plus_ten(x):
#     return x + 10
#
# print(plus_ten(10))

# 방법1
print((lambda x: x + 10)(10))

# 방법2
# plus_ten = lambda x: x + 10
# print(plus_ten(10))

# 리스트 [1,2,3] + 10 => [11,12,13]
# for문
li = [1,2,3]
new_list=[]
for i in range(len(li)):
    y = li[i] + 10
    new_list += [y]
print(new_list)

a = [1,2,3]
b = []
for i in a:
    p = i + 10
    b.append(p)
print(b)

a = [1,2,3]
b = []
for i in a:
    p = lambda x : x+10
    b.append(p(i))
print(b)

def plus_ten(x):
    return x + 10

b=[]
for i in a:
    p = plus_ten(i)
    b.append(p)
print(b)

# map(함수, 인수로사용될값들) : 함수를 여러번 수행하되 서로 다른 인수값들을 적용
#  반환type: map()객체
print('map()적용:', list(map(plus_ten, [1,2,3])))
print('map()적용:', list(map(lambda x: x+10, [1,2,3])))

# 리스트컴프리헨션 : [  for i in range() ]
a = [1,2,3]
b = [(lambda x : x+10)(i) for i in a]
c = [plus_ten(i) for i in a]
print(b)
print(c)
