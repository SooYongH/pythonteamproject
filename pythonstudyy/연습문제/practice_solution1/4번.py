from random import randint
dice1=randint(1,6)
dice2=randint(1,6)
dice3=randint(1,6)
dice4=randint(1,6)
dice5=randint(1,6)
dice6=randint(1,6)

count=1
while True:
    if dice1==dice2 and dice2==dice3 and dice3==dice4 \
        and dice4==dice5 and dice5==dice6 :
        break
    dice1 = randint(1, 6)
    dice2 = randint(1, 6)
    dice3 = randint(1, 6)
    dice4 = randint(1, 6)
    dice5 = randint(1, 6)
    dice6 = randint(1, 6)
    count+=1
print(f'6개 주사위의 눈은 모두 {dice1}')
print(f'주사위의 눈이 모두 같을 때까지 {count}회 던졌네요.')
