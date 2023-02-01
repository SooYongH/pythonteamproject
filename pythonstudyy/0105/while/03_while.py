#잔액이 소진될 때까지 노래하기
#금액 투입시키기
#1곡에 500원

print('웰컴투 숑노래방! 한 곡당 500원입니다~~')
print()
mon=int(input('금액을 투입하세요:'))
print()
num=1
while 1 :
    print(input('노래를 입력하세요'))
    print(f'노래를 {num}곡 불렀습니다.')
    mon -= 500
    if mon < 500 :
        print('잔액이 부족합니다. 종료합니다.')
        break
    else :
        print(f'현재 {mon}원 남았습니다.')

    num += 1
    print()

