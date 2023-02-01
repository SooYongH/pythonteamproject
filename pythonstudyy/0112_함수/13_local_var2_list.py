# 함수에 리스트 전달 : 리스트는 같은 리스트를 공유
# 함수내부에서 리스트 변경시 원본리스트도 변경
'''
def show_list(my_list):
    print('함수안: ', id(my_list))
    for x in my_list:
        print(x, end=' ')
    print()
    my_list[0]=100
'''

def show_list(my_list):
    print('함수안: ', id(my_list))
    for x in my_list:
        print(x, end=' ')
    print()
    my_list = [100, 200, 300]
    print('새로생성: ', my_list)
    print('함수안(새로생성): ', id(my_list))

def show_list(my_list):
    print('함수안: ', id(my_list))
    for x in my_list:
        print(x, end=' ')
    print()
    my_list2 = my_list.copy()
    print('새로생성: ', my_list2)
    print('함수안: ', id(my_list))
    print('함수안(새로생성): ', id(my_list2))


my_list = [10,20,30,40]
show_list(my_list)
print(my_list)
print('함수밖: ',id(my_list) )


