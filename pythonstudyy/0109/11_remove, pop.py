# 리스트 요소 삭제 메서드 : remove(), pop()

# remove(삭제값) : 첫번째 만나는 값을 삭제

data = [1,3,4,2,1,6,5,3,4,3]
data.remove(3)
print(data)

item = 3
while item in data:
    data.remove(item)
print(data)

# data.remove(item)
# 삭제할 요소가 없는 경우 오류(ValueError) 발생

# pop() : 리스트의 마지막 요소를 반환하고 삭제
value = data.pop()
print(data)
print(value)

data.pop()
data.pop()
data.pop()
print(data)

data.pop()
data.pop()
data.pop()
print(data)
# data.pop()
# print(data)

# pop(index) :지정한 인덱스의 요소를 반환하고 삭제
names = ['강감찬', '유관순', '홍길동', '안중근']
name = names.pop(2)
print(names)
print(name)