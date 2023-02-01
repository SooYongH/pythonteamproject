# 튜플(tuple) 생성
# 참고. 리스트 생성 : [] 또는 list()
l1 = list()
l2 = []
print(type(l1))

# 튜플생성 : () 또는 tuple()
t1 = (1,2,3)
print(t1)

t2 = 4,5,6
print(t2)

t3 = t1, (7,8,9)  # 튜플 내 튜플 포함
print(t3)

t4 = [1, 2], [3, 4]
print(t4)

t5 = tuple([5,6,7,8])
print(t5)
print(type(t5))

# 튜플을 리스트로 변환
to_list1 = list(t1)
print(to_list1)
to_list3 = list(t3)
print(to_list3)
print(type(to_list3[0]))
