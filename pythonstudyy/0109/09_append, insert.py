# 리스트 조작메서드 :
# 1. 요소 삽입 : append(), insert()

# append() : 리스트의 끝에 요소 추가
a = [1,2,3,4,5]
a.append(10)
print(a)

a.append([20,30])
print(a)

# insert(위치(인덱스), 값) : 리스트의 특정 위치에 값을 삽입

a.insert(3, 'apple')
print(a)
a.insert(-1, 'banana')
print(a)
a.insert(len(a), 'last')
print(a)


# 예제. 3명의 회원을 입력받아서 리스트에 추가하고 리스트 내용 출력
name_list = []

for _ in range(3):
    # name_list.append(input('회원 입력: '))
    # name_list.insert(len(name_list), input('회원 입력: '))
    name_list.insert(0, input('회원 입력: '))

print('회원명단 :', name_list)