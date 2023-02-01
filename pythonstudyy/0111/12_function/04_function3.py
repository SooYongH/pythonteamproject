# 함수의 매개변수와 인수

# 매개변수(parameter) : 함수의 입력값

# 예. 매개변수가 없는 함수
def add():
    x = int(input('num1: '))
    y = int(input('num2: '))
    return x+y

# 매개변수(parameter)가 있는 경우
def add(x, y):
    return x+y

# 함수가 호출될 때 함수의 입력값으로 사용되는 값을 인수(argument)라고 함
# 함수의 매개변수와 같은 위치에 있는 값들이 대응되어 전달
# print(add(1,2))


# 디폴트(default) 인수
#  => 매개변수에 기본값을 지정

def add(x, y=1):
    print(f'두수의 합은 {x+y}')

add(10,20)
add(10)

def greet(name, msg='Hi!'):
    print(name + ' ' + msg)

# 디폴트인수는 맨 뒤에 나와야 함
# def greet(msg='Hi!', name):
#     print(name + ' ' + msg)

greet('Kang', 'Hello')
greet('Hong')

def show_info(name, age=8, year=1):
    print(name, age, year)

show_info('Kang', 13, 6)
show_info('Hong', 8)
show_info('Kim')

