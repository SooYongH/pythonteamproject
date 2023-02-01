'''

def add():
    global a
    a+=1
    c=a+b
    print(a)
    print(b)
    print(c)
a=1
b=10
add()


def sun(x,y):
    global a
    a=7
    x,y=y,x
    b=3
    print(a)


std_info_list=[{'name':'hong','age':'30'},{'name':'kang','age':'20'},{'name':'kim','age':'10'}]

def get_std_info(std_info):
    name=std_info['name']
    age=std_info['age']
    std=get_std_info(std_info)
    return{'이름':}
어려워


def selfcall():
    print('ha', end=' ')
    selfcall()

selfcall()



add2=lambda x=10, y=20 : x+y
print(add2())
print(add2(5))

print((lambda x: x+10)(100))
y=5
print((lambda x: x+y)(100))

def plus_ten(x):
    return x+10
print(plus_ten(10))


a=lambda x:x+10
print(a(10))

print((lambda x : x+10)(10))

a=[1,2,3]
b=[]
for i in a:
    p=lambda x:x+10
    b.append(p(i))
print(b)


def plus_ten(x):
    return x+10
    '''

list1=[1,2,3,4]
list2=[10,20,30,40]
'''
def addList():
    total = []
    for i in range(len(list1)):
        add_data=list1[i]+list2[i]
        total.append(add_data)
    return total
print(addList())
'''
def addList(x,y):
    total = []
    for i in range(len(x)):
        total.append(x[i]+y[i])
    return total
print(addList(list1,list2))

print([(lambda x,y : x+y)(list1[i],list2[i]) for i in range(len(list1))])

print([x+y for x,y in zip(list1,list2)])

print(list(map(lambda x,y : x+y, [1,2,3,4],[10,20,30,40])))

print(list(map(lambda x,y : x+y, list1,list2)))

#추가필수!!!!!!!!!!!!!!!!!!!!!!!!!
# all 숫자 0이 아니면 T
# any 하나라도 참이면 T 모두 거짓이면 빈 문자열이면 F
print(chr(1))
print(chr(47))
print(chr(48))
print(chr(65))
print(chr(66))
print(chr(90))

print(ord('a'))
print(ord('*'))
print()

country = ["Korea", "Japan", "China"]
country.append("Remove")
print(country.remove("Remove"))