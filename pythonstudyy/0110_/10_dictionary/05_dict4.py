# in / not in 연산자

d = {'one':1, 'two':2, 'three':3, 'seven':7}
print('two' in d)
print('four' in d)
print('four' not in d)

#
for k, v in d.items():
    print(k, v)

for k in d.keys():
    print(k, d[k])


#한줄에 여러줄 쓰고 싶을 때 ;