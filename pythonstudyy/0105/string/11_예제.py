#하트문자 :'\u2665'
#입력한 숫자만큼의 하트를 출력하는 코드 작성
#for문과 문자열 응용

num=input('숫자를 여러개 입력하세요.')
length=len(num)
for i in range(0,length) :
    a=num[i]
    print('\u2665'*int(a))

# #random 넘버
# random.randint(1,100)
# from randon import randint
# randint(1,100)


