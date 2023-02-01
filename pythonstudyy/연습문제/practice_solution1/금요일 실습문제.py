#1
a=input('십진수 입력: ')
print(f'이진수는 0b{}')

#2
b=input('16진수 한 글자 입력 : ')
print(f'10진수')
#3
from random import randint
num=randint(1,10)
print(num)
yournum=int(input('숫자를 맞혀 보세요.(1~100):'))
while num!=yournum :
        if num>yournum :
            print('숫자가 낮아요.')
        else :
            print('숫자가 높아요.')
        newnum = int(input('숫자를 다시 입력하세요: '))

print(f'정답입니다! 입력한 숫자는 {num}입니다.')


#4
from random import randint
t1=randint(1,6)
t2=randint(1,6)
t3=randint(1,6)
t4=randint(1,6)
t5=randint(1,6)
t6=randint(1,6)

while 1 :
print(f'주사위 숫자가 모두 같을 때까지 {try}번 던졌어요!')
print(f'6개 주사위의 눈은 모두 {num}')
try+=1
    if t1=t2=t3=t4=t5=t6 :
        break

#5
for i in range(1,10,2):
    a='*'*i
    print('{:^10}'.format(a))


#6

#7
list=''
for i in range(10) :
    num=int(input(f'숫자{i}입력 : '))
    list=list+str(num)+' '
print('-------------')
an=list.split()
answer=int(an)

count1=count2=count3=0
for i in range(answer) :
    if i>0 :
        count1 += 1
        print(f'양수: {count1}개')
    elif i>0 :
        count2 += 1
        print(f'음수: {count2}개')
    else :
        count3 += 1
        print(f'0  : {count3}개')

#8
num=input('숫자를 여러개 입력하세요.')
length=len(num)
for i in range(0,length) :
    a=num[i]
    print('\u2665'*int(a))


