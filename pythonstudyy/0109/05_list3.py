#리스트의 값 변경
list_a=[10,20,30]
print('값 변경 전 list_a', list_a)
list_a[2]=200
print('값 변경 후 list_a', list_a)
list_a[1]=[200,300]
print('값 변경 후 list_a', list_a)

list_a[1:2]=[200,300]
print(list_a)

#그 자리 수가 삭제되고 넣고자 하는 수가 저장됨

#리스트 각각의 값을 변수에 저장
a,b,c,d=list_a
print(a)
print(b)
print(c)
print(d)