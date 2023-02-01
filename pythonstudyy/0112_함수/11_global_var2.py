# 전역변수를 함수내부에서 사용할 때 : global

def add():
    global a    # a :전역변수
    a = a + 1
    c = a + b   # b : 전역변수
    print(a)
    print(b)
    print(c)

a = 1
b = 10
add()
