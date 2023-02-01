#파일 쓰기모드 :'a' => append 뒤에 붙여쓰기

f=open('data/outfile2.txt','a',encoding='utf-8')
s=input('문자열 입력: ')
f.write(s)

s=input('문자열 입력: ')
f.write(s)

s=input('문자열 입력: ')
f.write(s)
f.close()
