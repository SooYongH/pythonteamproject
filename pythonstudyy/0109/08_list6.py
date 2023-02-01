# 1.리스트의 요소 삭제 :
# del(리스트요소) 또는 []연산자

list_a = [10, 20, 30, 40, 50, 60, 70]
print('삭제 전:', list_a)

del(list_a[1])
print('del(list_a[1]) 삭제 후:', list_a)

list_a[1:3] = []
print('list_a[1:3] =[] 사용한 후:', list_a)

# 리스트 자체를 삭제
list_b = ['a','b','c']
# list_a = []
list_a = None
print(type(list_a))
print(list_a)
del(list_b)
# print(list_b)