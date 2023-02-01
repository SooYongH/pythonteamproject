# 튜플 인덱싱, 슬라이싱

t = (1,2,3,4,5,6,7)
print(t[0])
print(t[:])
print(t[::-1])

# 변경여부 확인 : 변경, 추가, 삭제 불가
# t[1]=10
# t.append(4)
# del(t[1])

# 튜플에서 사용하는 메소드 : count(), index()
t2 = ('h', 'e', 'l', 'l', 'o', 'h', 'i')
# t2 = tuple('h e l l o h i'.split())
print(t2)
print('h갯수 :',t2.count('h'))
print('h의 인덱스 :',t2.index('h'))

# 튜플 삭제
del(t2)
print('t2 삭제')
# print(t2)

ch_list = []
for c in 'hello':
    ch_list.append(c)
print(ch_list)