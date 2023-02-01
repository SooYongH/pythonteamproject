#with문을 사용한 파일입력&출력
#close 없어도 됨 간소화됨
with open('data/study.txt','r',encoding='utf-8')as f:
    test=f.read()
    print(test)

with open('data/outfile4.txt','a') as f2:
    f2.write('\nPython')

with open('data/outfile4.txt','r',encoding='utc-18') as f3:
    testing=f3.read()
    print(testing)