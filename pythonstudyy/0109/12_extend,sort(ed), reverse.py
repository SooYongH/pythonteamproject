# 리스트 확장 : extend()

data = [1,2,3]
data.extend([4,5,6])
print(data)

data.append([10,11,12])
print(data)

data.append(7)
print(data)

data.extend([10,11,12])
print(data)

print()
# 리스트 정렬 :
#  sort(), reverse() : 리스트의 객체 메서드
#  sorted() : 파이썬 내장함수

# sort() 메서드 : 정렬, 원본 리스트를 변경
num_list = [85,97,50,60,30,100,75]
print(num_list)

num_list.sort()
print(num_list)

num_list = [85,97,50,60,30,100,75]
num_list.sort(reverse=True)
print(num_list)

# sorted() 함수 사용 : 원본그대로 유지
print('정렬:sorted()===========')
num_list = [85,97,50,60,30,100,75]
result = sorted(num_list, reverse=True)
print(result)
print(num_list)

# reverse() :역순으로 , 원본리스트 변경
num_list.reverse()
print(num_list)

print('==========================')
# 다양한 데이터를 갖는 리스트의 정렬 예
ch_list = ['a', 'c', 'a', 'f', 'z', 'i']
ch_list.sort(reverse=True)
print(ch_list)

ch_list = ['A', 'C', 'A', 'F', 'Z', 'I']
ch_list.sort()
print(ch_list)

ch_list = ['f', 'C', 'a', 'F', 'z', 'I']
ch_list.sort()
print(ch_list)

str_list = ['Blue', 'cyan', '하양', 'yellow','노랑', 'magenta', 'market', 'GReen']
str_list.sort()
print(str_list)
