#for문 이용하여 다음의 내용을 갖는 텍스트 파일(outfile3.txt)을 출력하기

#1행
#2행
#3행
#4행
#..
#10행

f=open('data/outfile3.txt','w',encoding='utf-8') #ansi코드로 저장될 것
s=''
for i in range(1,11):
    s+=str(i)+'행\n'
f.write(s)

# for i in range(1,11):
#     s=str(i)+'행\n'
#     f.write(s)

f.close()
