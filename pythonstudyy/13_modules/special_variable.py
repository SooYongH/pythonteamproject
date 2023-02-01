name=''

def set_name():
    global name
    name=input('너의 이름은? ')

def get_name():
    if name =='':
        return '무명'
    else:
        return name

#이 파일이 모듈로 사용될 시, __name__의 값은 __main이 아니어서 이 부분이 수행되지 않음
#파이썬에서 제공하는 스페셜 변수 __name__: 현재 파일이 실행될 경우, 값은 __main__을 갖게됨
print('__name__=', __name__)
#해당 파일 내에선 __main__/ 모듈 불러와서 실행한 파일 내에선 이 파일명이 찍힘
if __name__=='__main__':
    set_name()
    print(get_name())