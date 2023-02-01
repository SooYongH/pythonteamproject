# 재귀함수(recursive function)
# 자신의 함수안에서 자신의 함수를 호출

def selfcall():
    print('ha', end='')
    # selfcall()    # 무한호출 : stackoverflow발생 따라서 if조건 필수
# selfcall()

# 1부터 10까지 더하기
def add(n):
    if n==1:
        return 1
    return n + add(n-1)
이해안됨//

print(add(10))

# 문제. 팩토리얼 계산하는 함수 fact()를 재귀함수로 작성
# 팩토리얼(factorail) : 0!=1. 1! =1
# 10! = 10 * 9 * 8 * ... * 1
# n! = n*(n-1)*(n-2)*...*2*1

def fact(n):
    if n==1:
        return 1
    return n*fact(n-1)

print('10!=',fact(10))
이해안가아아ㅏ

# 숙제. 피보나치수열을 만드는 재귀함수로 작성
# 0, 1
# fibo(1) + fibo(2) = fibo(3)