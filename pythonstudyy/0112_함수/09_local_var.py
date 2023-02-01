# 지역변수(local variable) : 함수내부에서 사용하는 변수
'''
# 지역변수1
def show():
    a = 1       # a: 지역변수
    print(a)

# 지역변수2
def show():
    a = 1       # a: 지역변수
    a = a+1
    print(a)

# 지역변수3
def show(a=5):
    a = a+1     # a : 지역변수
    print(a)

a = 10
# show(a)
show()

# 지역변수4
def show():
    a = a + 1     # a : 지역변수 : 값이 지정되지 않아 연산불가 (UnboundLocalError)
    print(a)

a = 10  # 전역변수
show()

# 지역변수5
def show():
    print(a)    # a : 전역변수

a = 10  # 전역변수
show()
'''
# 지역변수6
def show():
    a = 100
    print(a)    # a : 지역변수

# show(a)   # a: 전역변수
