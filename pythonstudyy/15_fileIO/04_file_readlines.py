#텍스트파일 처음부터 끝까지 전부 읽기 : readlines()

f=open('data/study.txt','r',encoding='utf-8')

lines=f.readlines()
print(lines)
#우리가 엔터를 쳤기에 매줄 마지막엔 \n이 포함되어 있음
for line in lines:
    # print(line,end='')
    print(line.strip('\n'))
    #끝에 \n없애는 법 두가지
# print(type(lines))
f.close()

f2=open('data/study.txt','r',encoding='utf-8')
for line in f2:
    print(line,end='')
f.close()