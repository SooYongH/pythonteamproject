#파일 전체 읽기:readline()

f=open('data/study.txt','r',encoding='utf-8')

while 1:
    line=f.readline()
    #한줄씩 다 읽어오는것
    if not line :  #파일의 끝
        break
    print(line)

f.close()
