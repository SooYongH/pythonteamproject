#set 생성
'''
s1={1,2,3,1,3,4}
print(s1)
print(type(s1))

s1.add(10)
print(s1)

# s1.add([8,9])
s1.update([8,9])
print(s1)

s1.discard(7)
print(s1)
# s1.remove(7)

for i in range(3):
    print(s1.pop())
print(s1)

#합집합 A|B A.union(B)
#교집합 A.intersection(B)
#차집합 A.differnece(B)


partyA= {'park','kim','lee'}
partyB= {'park','hong', 'kang'}

partypeople=partyA.intersection(partyB)
partypeople=partyA&partyB
print(partypeople)

yeah=partyA.union(partyB)
yeah=partyA|partyB
print(yeah)

onlya=partyA.difference(partyB)
onlya=partyA-partyB
onlyb=partyB.difference(partyA)
onlyb=partyB-partyA
print(onlya)
print(onlyb)



names = ['kim', 'hong', 'lee', 'choi']
foods = ['오뎅', '라면', '순대국', '파스타', '피자']
drinks = ['사이다', '콜라', '커피', '홍차']

pairList=list(zip(names,foods))
pair2=dict(zip(names,foods))
print(pairList)
print(pair2)


num_list=[num for num in range(1,11) if num%2==0]

num_list2=[x+y for x in range(10) for y in range(10)]
print(num_list2)

list3=[(x,y) for x in ['커피','우유','콜라'] for y in ['사과','바나나','딸기','키위']]
print(list3)

stds=['철수','영희','길동','순희']
scores=[50,60,90,80]
dict_std2=dict(zip(stds,scores))

print(dict_std2)

for n,s in dict_std2.items():
    if s>=60:
        print(n,s)

dict_std3={n:s for n,s in dict_std2.items() if s>=60}
print(dict_std3)


dict_std5={n:'P' if s>=60 else'F' for n,s in dict_std2.items()}
print(dict_std5)



def show():
    a=int(input('숫자를 입력:'))
    b= int(input('또다른 숫자를 입력:'))
    total=a+b
    print(f'합: {total}')
    return a+b
show()

def get_area():
    w=int(input('가로 길이를 입력: '))
    h= int(input('세로 길이를 입력: '))
    return w*h
print(f'사각형의 면적 = {get_area()}')


def get_info():
    name= input('이름 입력:')
    age = input('나이 입력:')

    return {'name':name, 'age':age}

std_info =get_info()
print(std_info)


def add(x,y=1):
    print(f'두수의 합은 {x+y}')
    return x+y
print(add())
add(10,20)
add(10)



def show_info(name, age=8, year=1):
    print(name, age, year)

show_info('kang',13,6)
show_info('kang',13)
show_info('kang')

def show_info(info):
    print(info)
    print('이름 '+info['name'])
    print('나이 '+info['age'])
    for k,v in info.items():
        print(k,':',v)

info={'name':'kang','age':'20'}
show_info(info)


def add(*args):
    pass
# add(1)
# add(1,2)
# add(1,2,3,4,5,6,7,8,9)

def order_coffee(coffee,*options):
        print(coffee,'옵션:',end=' ')
        for x in options:
            print(x, end=' ')
        print()
order_coffee('아샷추','톨사이즈','얼음조금','샷2번추가')


def add(*num):
    total = 0
    for i in num:
        total+=i
    print(total)
    print()

add(1)
add(2,3)
add(1,2,3)
add(4,5,6,7,8,9)


def info(a,b,c):
    print(a,b,c)

info(3,4,5)
info(b=10,c=4,a=1)
info(c=10,a=4,b=1)


def info(**kwargs):
    for k,v in kwargs.items():
        print(k,':',v, end=' ')
    for k in kwargs.keys():
        print(k, end=' ')
    for v in kwargs.values():
        print(v, end=' ')
    print()


info(b=10)
info(c=10,a=1,b=5)

def info(a,b,*args, **kwargs):
    print(a,b)
    print(args)
    print(kwargs)

info(1,2,3,4,c=5,d=6)
def info(a,b,*args,**kwargs):

'''

