# 두 리스트의 같은 위치 요소들의 합 구하기

list1 = [1,2,3,4]
list2 = [10,20,30,40]
print(zip(list1,list2))

def addList(x,y):
    result = []
    for i in range(len(x)):
        result.append(x[i]+y[i])
    return result

print(addList(list1, list2))

print(list(map(lambda x,y: x+y, list1, list2)))

print(list(map(lambda x,y: x + y,[1,2,3,4],[10,20,30,40])))

print([(lambda x,y : x+y)(list1[i],list2[i]) for i in range(len(list1))])

def addlist(x,y):
    return [x + y for x, y in zip(list1, list2)]
print(addlist(list1,list2))

print([x + y for x, y in zip(list1, list2)])


a = list1.copy()
b = list2.copy()
c = {}
for i in range(len(a)):
    c[a[i]] = b[i]
print(c)
d = [(lambda x, y:x+y)(i, j) for i,j in c.items()]
print(d)