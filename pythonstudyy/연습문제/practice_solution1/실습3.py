from random import randint
com_num=randint(1,100)
user_num=int(input('숫자를 맞혀보세요(1~100) :'))

while com_num != user_num :
    if user_num > com_num :
        print('숫자가 높아요')
    else:
        print('숫자가 낮아요')
    user_num = int(input('숫자를 다시 입력하세요 : '))
print(f'정답입니다! 입력한 숫자는 {com_num}입니다.')