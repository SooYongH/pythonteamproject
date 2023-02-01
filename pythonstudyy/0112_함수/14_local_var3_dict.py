# 함수의 인수로 딕셔너리가 전달되는 경우

std_info_list = [{'name':'hong', 'age':30, 'year':1, 'major':'sci'},
            {'name':'kang', 'age':20, 'year':2, 'major':'bigdata'},
            {'name':'kim', 'age':25, 'year':3, 'major':'edu'}]

def get_std_info(std_info):
    name = std_info['name']
    age = std_info['age']
    print('함수내부:',id(std_info))
    print(std_info)
    return {'이름':name, '나이':age}

for std_info in std_info_list:
    print('함수외부:',id(std_info))
    print('함수외부:',type(std_info))
    std = get_std_info(std_info)
    for k in std.keys():
        print(std[k], end=' ')
    print()