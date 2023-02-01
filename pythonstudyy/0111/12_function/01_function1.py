# 함수 정의 및 호출

# 1. 함수 정의
def show_welcome():
    print('welcome!!!!')

# 2. 함수호출
show_welcome()


def show_info():
    # print('name: Hong')
    # print('age: 20')
    pass

show_info()

# 문제1. 정수 2개를 입력받아 두 수의 합을 구하고 출력함수 add() 정의 및 호출
# 숫자1 입력: 3
# 숫자2 입력: 4
# 합 : 7

def add():
    x = int(input('숫자1입력: '))
    y = int(input('숫자2입력: '))
    print('합 :', x+y)

# add()
# z = add()
# print(z)

# 함수의 반환값 : return
#   => 함수 호출하고 결과값을 받을 수 있게 함
#  변수명 = 함수()

def add2():
    x = int(input('숫자1입력: '))
    y = int(input('숫자2입력: '))
    # print('합은', x+y)
    return x+y    # 결과값 반환

# z = add2()
# print('합 : %d' % z)

# return 문 주의!!
# return문은 한개만 사용할 것
# return문이 여러개 있는 경우 맨처음 return문만 수행됨

def multi_return():
    return 1
    return 2
    return 3

result = multi_return()
print(result)


