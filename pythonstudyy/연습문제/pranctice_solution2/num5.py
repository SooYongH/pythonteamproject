def decToBin(decimal):
    res=''
    while decimal>0 :
        res=str(decimal%2)+res
        decimal=decimal//2
    return res

def binToDec(bin):
    n=len(bin)
    decimal=0
    for i in range(n):
        decimal+=int(bin[i]) * 2**(n-i-1)  #i는 각 숫자의 인덱스 위치 0부터 시작
    return decimal

result1=decToBin(10)
print(result1)
print(binToDec('1010'))

#2진수를 10진수로 바꾸는 법
