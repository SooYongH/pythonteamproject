# 딕셔너리의 주요 메서드

d = {'one':1, 'two':2, 'three':3}
print(d['two'])
# print(d['ten'])
# [] 연산자를 이용하여 키의 값을 가져올 경우 없는 키를 사용할 때 오류발생

# get() : 키에 대한 값을 가져옴, 키가 없는 경우 None 반환
print(d.get('two'))
print(d.get('ten'))
print(d['one'])

# copy() : 복사
print('shallow copy========')
d2 = d
print(id(d))
print(id(d2))
d2['1']=100
print(d)

print('deep copy=========')
d2 = d.copy()
print(id(d))
print(id(d2))

# immutable (변경불가) : int, float, tuple
print('참고. immutable의 경우')
x=3
y=x
print(id(x))
print(id(y))
y = y+3
print(id(y))
print(id(x))

# 참고. 리스트의 deep copy
l1 = [1,2,3]
l2 = l1[:]
print(id(l1))
print(id(l2))

# update() : 두 딕셔너리를 한 딕셔너리로 결합
print('---update()---------')
d3 = {'nine':9, 'ten':10}
d.update(d3)
print(d)

# popitem() : 딕셔너리의 맨마지만 키와 값을 튜플형식으로 가져온 뒤 삭제
print('--popitem()----')
print(d3)
print(d3.popitem())
print(d3)
k, v = d3.popitem()
print(k, v)
print(d3)

# pop(키) : 지정한 키를 값는 item의 값을 반환후 딕셔너리에서 제거
print('--pop()----')
d = {'one':1, 'two':2, 'three':3}
print(d)
print(d.pop('one'))
print(d)

# setdefault() : 딕셔너리[키]=값 같은 효과
print('--setdefault()------')
d = {'one':1, 'two':2, 'three':3, 'seven':7}
print(d)
print(d.setdefault('ten', 10))
print(d)

# clear() : 모든 아이템을 다 제거 => 빈 딕셔너리 반환
print('--clear()--------')
print(d)
d.clear()
print(d)