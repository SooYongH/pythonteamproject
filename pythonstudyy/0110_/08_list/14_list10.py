# 리스트 조작 :
# max(), min() 함수

list1 = [100, 75, -30, 90, 65]
list2 = ['a', 'A', 'C', 'z', 'd']

print('list1의 최대, 최소요소')
print('최대',max(list1))
print('최소',min(list1))

print('list2의 최대, 최소요소')
print('최대',max(list2))
print('최소',min(list2))

# index(요소) :리스트안의 요소의 위치 반환

names = ['홍길동', '슈퍼맨', '성춘향', '피노키오']
print(names.index('슈퍼맨'))
# print(names.index('원더우먼'))   # 요소가 없는 경우 오류 발생

# in/ not in
name = '원더우먼'
if name in names:
    print('찾는 인덱스는:', names.index(name))
else:
    print('리스트에 존재하지 않습니다')

# 비교연산 ==, !=, > , <

list3 = [1, 2, 3]
list4 = [1, 2, 4]
print(list3 == list4)
print(list3 != list4)
print(list3 >= list4)
print(list3 < list4)

