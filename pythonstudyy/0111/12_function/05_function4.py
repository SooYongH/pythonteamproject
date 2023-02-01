# 함수에 리스트를 전달하는 경우
def show_names(names):
    for name in names:
        print(name, end=' ')

name_list = ['Kang', "Hong", 'Lee', 'Park']
show_names(name_list)

#
def show_info(info):
    print(info)
    # print('이름: ' + info['name'])
    # print('나이:' , info['age'])
    for k, v in info.items():
        print(k,':', v)

info = {'name':'Kang', 'age':20, 'email':'aaa@email.com'}
show_info(info)