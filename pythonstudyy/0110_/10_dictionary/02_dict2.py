# 딕셔너리의 뷰(view)
# : 딕셔너리의 키(key), 값(value), 항목(item) 반환

d = {'one':1, 'two':2, 'three':3}
d2 = {1:'one', 2:'two', 3:'three'}

print(d['one'])
d[1]='one'
print(d)
print(d[1])

# 딕셔너리의 키(key)값들을 보여주고 반환
#  : 딕셔너리변수.keys()
#     => dict_keys() 타입으로 반환
print('##딕셔너리 키(key)###')
print(d.keys())
print(type(d.keys()))
print(list(d.keys()))

for key in d.keys():
    print(key)

# 딕셔너리의 값(value)에 대한 뷰
#  : 딕셔너리변수.values()
#   => 딕셔너리의 값들을 반환 (dict_values 타입)

print('##딕셔너리 값(value)###')
print(d.values())
print(list(d.values()))

for value in d.values():
    print(value)

# 딕셔너리의 항목(item)에 대한 뷰
#  : 딕셔너리변수.items()
#   => 딕셔너리의 키와 값의 쌍(튜플로 묶여있음)들을 반환 (dict_items 타입)

print('##딕셔너리 항목(item)###')
print(d.items())
print(list(d.items()))

for k,v in d.items():
    print(k, v)