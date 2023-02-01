# 리스트 복사

# 얕은 복사(shallow copy)
scores = [50, 60, 80, 90, 75]
print('리스트 값 변경 전')
c_scores = scores
print(scores)
print(c_scores)

scores[0] = 95
print('리스트 값 변경 후')
print(scores)
print(c_scores)

c_scores[-1] = 100
print('리스트 값 변경 후2: ')
print(scores)
print(c_scores)

# 깊은 복사(deep copy) : list()
values = list(scores)
print('values:', values)
scores[1] = -100
print(scores)
print(c_scores)
print(values)

# deepcopy()
# import copy
from copy import deepcopy
a = ['a', 'b', 'c']
b = deepcopy(a)
b[0] = 10
print('a', a)
print('b', b)