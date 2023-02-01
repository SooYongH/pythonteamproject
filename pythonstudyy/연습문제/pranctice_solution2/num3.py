words={}
while 1:
    eng=input('영어 단어 등록 (종료는 quit) : ')
    if eng=='quit':
        break
    elif eng in words.keys():
        print(f'{eng}는 이미 등록된 단어 입니다.')
        print()
        continue
    han=input('{}의 뜻입력 (종료는 quit) : '.format(eng))
    words[eng]=han
    print()


while 1:
    search=input('\n검색할 단어 입력 (종료는 quit) : ')
    if search=='quit':
        print()
        print('종료합니다.')
        break
    elif search in words.keys():
        print(f'{search}의 뜻은 {words[search]}입니다')
        print()
    else:
        print(f'{search}는 사전에 없는 단어 입니다.')
        print()