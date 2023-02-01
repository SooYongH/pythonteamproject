#csv 파일읽기
#쪼개서 분류화하기
import csv
# with open('data/sample3.csv','r',encoding='utf-8') as f:
#     # print(f.read())
#     data=csv.reader(f)
#     print(data)
#
#     for x in data:
#         print(x)

# f=open('data/sample3.csv','r',encoding='utf-8')
# data=csv.reader(f)
# datalist=[]
# for x in data:
#     datalist.append(x)
# print(datalist)
# f.close()

def opencsv(filename,encode='utf-8'):
    f=open(filename,'r',encoding=encode)
    data=csv.reader(f) #읽어라
    datalist=[]
    for d in data:
        datalist.append(d) #추가해라
    f.close()
    return datalist #내보내라

data=opencsv('data/sample3.csv')
print(data)