def fact1(n):
    fact=1
    for i in range(1,n+1):
        fact*=i
    return fact


def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print('10!=',fact(10))

n=5
print(fact1(n))
print(fact(n))