# 가변길이 매개변수 : **kwargs
# key=value 의 형식으로 실인수가 여러개 전달
def info2(**kwargs):
    print(type(kwargs))
    for k,v in kwargs.items():
        print(k,':',v)
    for k in kwargs.keys():
        print(k, end=' ')
    print()
    for v in kwargs.values():
        print(v, end=' ')
    print()

info2(b=10)
info2(c=10, a=4, b=1)
