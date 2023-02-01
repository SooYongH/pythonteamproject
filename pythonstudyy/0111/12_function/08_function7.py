# 위치인수와 키워드인수
# 함수의 매개변수에 실인수를 지정할 때 매개변수이름 = 값의 형식으로 전달
# 매개변수명=값의 순서를 바꾸어도 됨
def info(a, b, c):
    print(a,b,c)

info(3,4,5)  # 위치인수(positional argument)
info(b=10, c=4, a=1) # 키워드인수(keyword argument)
info(c=10, a=4, b=1)

# 위치인수와 키워드인수가 함께 사용 가능하다
info(10, c=4, b=1)

# 위치인수는 키워드인수 보다 앞에 두어야한다
# info(a=4, b=1, 10)  # SyntaxError:positional argument follows keyword argument

# print(3,4,5, end=' ')

# 위치인수, 키워드인수, *args, **kwargs
# *args, **kwargs는 위치인수 뒤에 두고
# *args 다음에 **kwargs가 오도록 한다
print('----------------------')
def info(a, b, *args, **kwargs):
    print(a, b)
    print(type(a))
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

info(1,2,3,4,5,6, c=5, d=6)

