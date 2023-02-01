#파일 내에서 검색 : seek(offset,whence)함수
#offset : 상대 위치(whence위치서부터의 n번째 위치)
#whence : 0=시작위치,1=현재위치,2=파일의끝
#한글의 경우 utf-8은 3바이트가 한문자
#utf-16은 2바이트가 한문자
f=open('data/sample.txt','r',encoding='utf-8')

f.seek(0,0) #시작 위치 : 0행 0열
lines=f.readlines()
print(lines)

f.seek(6,0)
lines=f.readlines()
print(lines)

f.seek(7,0) #문자 위치 : 7번째 커서부터
lines=f.readlines()
print(lines)

f.seek(10,0) #문자 위치 : 7번째 커서부터
lines=f.readlines()
print(lines)

f.close()

