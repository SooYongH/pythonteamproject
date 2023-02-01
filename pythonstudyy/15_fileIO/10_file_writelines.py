#파일쓰기 : writelines()

list1=['Hi','Hello\n','Apple','100','200']
f=open('data/outfile4.txt','w')
f.writelines(list1)
f.close()
