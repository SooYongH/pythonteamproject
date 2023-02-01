n=int(input('생성할 피보나치 수열의 개수는? :'))
a=0
b=1
print(a,b,end='')
for i in range(n-2):
    fibo_n=a+b
    print(fibo_n, end=' ')
    a,b=b,fibo_n
print()