#7을 입력할 때까지 계쏙 입력하는 프로그램

a=int(input('숫자 입력 : '))
while a != 7 :
    a = int(input('다시 입력 : '))

print('7입력! 종료')

# #while True = while 1 버전

while True :
    a = int(input('숫자 입력 : '))
    if a == 7:
        print('7입력! 종료')
        break

#무한반복 구조를 활용해서 키보드로 알파벳 입력받되, 'q'를 입력하면 종료하기

while True:
    a=input('알파벳을 입력하세요 : ')
    if a=='q':
        print('종료하겠습니다.')
        break