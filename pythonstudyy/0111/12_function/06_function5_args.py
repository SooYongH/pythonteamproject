# 가변길이 매개변수 : *args
def add(*args):
    pass

# add(1)
# add(1,2)
# add(3,4,5)
# add(12,2,3,4,5,6)

def order_coffee(coffee, *options):
    print(coffee + ', 옵션: ', end=' ')
    for opt in options:
        print(opt, end=' ')
    print()

# order_coffee('아메리카노', 'Tall', 'Ice' )
# order_coffee('아메리카노')
# order_coffee('아메리카노', 'Tall', 'Ice', '시럽' )

# 문제. 1개 이상인 정수값들을 더하는 함수 add() 정의 (가변길이 매개변수 사용)
def add(*args):
    # print(type(args))
    total = 0
    for x in args:
        total += x
    print(f'합은 {total}')

add(1)
add(1,2,3)
add(3,4,5,6,7,8)
add()
