# 전역변수를 함수내부에서 사용
# 전역변수는 모든 곳에서 사용 가능

def show():
    c = a + b   # a, b : 전역변수
    print(a)
    print(b)
    print(c)

a = 10
b = 20

def add():
    print(a + b)   # a, b : 전역변수

show()
add()
print(a)
print(b)

