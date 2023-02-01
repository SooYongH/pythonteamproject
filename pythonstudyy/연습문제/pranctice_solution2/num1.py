import random
idiom=['개과천선','구사일생','군계일학','무용지물','동고동락',
       '유비무환','입신양명','괄목상대''막역지우','고장난명']
meaning=['잘못을 고치고 옳은 길에 덜어섬','죽일 고비를 여러 번 겪으며 살아나다',
         '평범한 사람 가운데 뛰어난 사람','아무짝에나 쓸모 없는 것','고통과 즐거움을 함께 한다',
         '미리 준비해두면 근심 걱정이 없다','사회적으로 인정받고 출세하여 이름을 세상에 드날림',
         '다른 사람의 학식이나 업적이 크게 진보한 것을 말함','생사를 같이 할 수 있는 친밀한 벗',
        '상대 없이 혼자서는 어떤 일을 이룰 수 없다']

print('사자성어 맞추기 게임을 시작합니다')
print('________________')
n=len(idiom)
i=random.randrange(n) #r해당 범위 내에서 랜덤으로 뽑아내도록하는 것 0~8까지

while True:
    print(meaning[i])
    answer=input('이 말의 사자 성어는?: ')

    if answer == idiom[i] :
        print()
        print('맞습니다...게임을 종료합니다. ')
        break
    else:
        print()
        print('틀렸습니다...다시 도전하세요 ')
        # i=random.randrange(n) 다른문제
        print()

# idiomzip=dict{}
# idiom:meaning}

# idiomzip=list(zip(idiom,meaning))
# print(idiomzip[0])
#
# from random import randint
# asking=randint(idiomzip[0],idiomzip[10])
# print(asking)
#     while True:
#     print(asking)
#     answer=input('이 말의 사자성어는? : ')
#     if asking==answer:
#         print('맞습니다.. 게임을 종료합니다.')
#         break
#     print('틀렸습니다...다시 도전 !')
#     print()
#
#
#
#
