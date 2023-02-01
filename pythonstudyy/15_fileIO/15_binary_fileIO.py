#이진파일 읽고 쓰기
inF=open('data/sample.PNG','rb') #읽고
outF=open('copy,PNG','wb') #씀

while True:
    inS=inF.read(1)
    if not inS:
        break
    outF.write(inS)

inF.close()
outF.close()

똥