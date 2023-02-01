#텍스트파일 읽기: readline()
#텍스트파일을 한줄씩 읽어옴

f=open('data/study.txt','r',encoding='utf-8')
line=f.readline()
print(line)
line2=f.readline()
print(line2)
f.close()