# 문제. global 키워드사용해서 함수내부에서 전역변수를 접근사용

def sub(x, y):
    global a
    a=7
    x,y=y,x
    b=3
    print('함수안:',a,b,x,y)
    print('a:', id(a))
    print('x:', id(x))

a,b,x,y=1,2,3,4
sub(x,y)
print('함수밖:',a,b,x,y)
print('a:', id(a))
print('x:', id(x))
