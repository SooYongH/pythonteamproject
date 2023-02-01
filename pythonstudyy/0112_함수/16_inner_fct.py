# 내부함수 : 함수안에 함수정의

def outFunc():
    def inFunc():
        print('inner function')
    print('out function', inFunc())

print(outFunc())

def outFunc2(x,y):
    def inFunc(a,b):
        return a+b
    return inFunc(x,y)

print(outFunc2(10, 20))
# print(inFunc(10, 20))
