#try~except~else문

try:
    num=int(input('숫자입력: '))
except ValueError as e:
    print('정수가 아닙니다',e)
else:
    print(num)

try:
    f=open('exception.txt','r')
except FileNotFoundError as e:
    pass
else:
    data=f.read()
    print(data)
    f.close()

print('종료') #요거랑 04finally랑 똑같