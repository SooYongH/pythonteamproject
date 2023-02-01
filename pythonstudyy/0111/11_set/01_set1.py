# set의 특징
# - 순서가 없다 (입력과 출력의 순서가 다를 수 있다)
# - 동일한 요소가 중복될 수 없다
# - 인덱스 사용 불가
# - 요소 추가/삭제 가능
# - 집합 안에 변경 가능한 항목 포함할 수 없음 : 튜플 포함 가능
#     리스트 포함 불가

# set 생성 : {1,} , set()
s1 = {1,2,3,1,3,4}
print(s1)
print(type(s1))

s2 = set([10,20,30])
print(s2)

s3 = set((500,300,200))
print(s3)

# 동일한 요소 중복 불가
s4 = {1,2,3,3,3,1}
print(s4)

# 집합 안에 변경가능한 요소 포함 불가
# s5 = {1,2,[3,4]}   # 에러 : TypeError
# print(s5)

# 인덱스 사용 불가
# s4[1]  # 에러

# 집합안에 변경불가한 요소 포함 가능
s6 = {(1,2),3,4}
print(s6)

# - 요소 추가/삭제 가능
# 요소추가 : add() 메서드
s6.add(10)
print(s6)
# s6.add([11,12]) # 에러 발생
# print(s6)

#요소 추가 :update() 리스트를 일반 set로 추가 가능케함
s6.update([5,6])
print(s6)

# 요소 삭제 : clear(), discard(), pop(), remove()

s = {1,2,3,4,5,6,7,8,9}
s.clear()
print(s)

s = {1,2,3,4,5,6,7,8,9}
s.discard(3)
print(s)
print('---------')
s.discard(11)   # 없는 요소를 삭제하려고 할 경우 오류없이 None
print(s)

s.remove(4)
print(s)

# s.remove(11)  # 없는 요소 삭제시 KeyError
# print(s)

# pop() : 첫번째(?) 요소 반환 후 제거
for i in range(3):
    print(s.pop())
    print(s)