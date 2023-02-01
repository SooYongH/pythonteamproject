# 리스트 연산
#인덱싱, 슬라이싱, + /* /in/ not in/len()

#+연산자
a=[1,2,3]
b=[4,5,6]
print(a+b)

#*연산자
c=[40,50,60]
d=c*3
print(d)

# 리스트 복사 (shallow copy)
scores=[50,60,80,90,75]
c_scores=scores
print(c_scores)

scores[0]=95
print(c_scores)
print(scores)

# 리스트 복사 (deep copy) : 새롭게 list를 생성
values=list(scores)
print('v ',values)
scores[-1]=-100
print(c_scores)
print(scores)
print(values)

#deepcopy
from copy import deepcopy
a=['a','b','c']
b=deepcopy(a)
b[0]=100
print('a'=a)



