#sample2.txt : ANSI 저장_한글은 2바이트
f=open('data/sample2.txt','r')
f.seek(7,0)
line=f.readline() #한줄만
print(line)

f.seek(16,0)
line=f.readline() #한줄만
print(line)


f.seek