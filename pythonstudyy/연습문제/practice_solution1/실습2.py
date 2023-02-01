a=input('16진수 한 글자 입력 : ')
num='123456789ABCDEFabcdef'
if a in num :
    print(f'10진수 ==> {int(a,16)}')
    #a를 16진수로 바꿔라
else :
    print('16진수가 아닙니다.')