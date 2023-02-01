# 반환값이 여러 개인 함수 정의 및 호출

# 반환값이 튜플 형식인 경우
def multi_return():
    return 1,2,3

# value = multi_return()
# print(value)
# print(type(value))
# x,y,z = multi_return()
# print(x,y,z)

# 반환값이 리스트인 경우

# 예. 5명의 이름을 입력받아 리스트로 저장하고 반환
# def get_names():
#     names = []
#     for i in range(5):
#         name = input('이름입력: ')
#         names.append(name)
#     return names

def get_names():
    names = [input('이름입력: ') for i in range(5)]
    return names

# x = get_names()
# print(x)

# 반환값이 딕셔너리인 경우
def get_info():
    name = input('이름입력: ')
    age = input('나이입력: ')

    return {'name':name, 'age':age}

# std_info = get_info()
# print(std_info)
# print(type(std_info))

# 반환값이 없는 경우 함수 호출하여 print()하면 None 출력
def show():
    print('return문이 없어요')
# x = show()
# print(x)
# print(show())

# 반환값이 하나인 경우
def get_digit():
    num = int(input('정수입력: '))
    return num

print(get_digit())