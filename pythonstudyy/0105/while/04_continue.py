#continue문
#반복분 수행 중에 continue문을 만나면 현재 시점에서 중단하고(다음 문장을 실행하지 않고 다시 반복을 진행)

#10 이하의 홀수 출력하기
# while문
i=1
while i<=10 :
    if i%2==0 :
        i += 1
        continue
    print(i, end=' ')
    i += 1
