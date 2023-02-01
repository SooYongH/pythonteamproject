#csv 파일 읽고쓰기 모듈

import csv

def opencsv(filename,encode='utf-8'):
    f=open(filename,'r',encoding=encode)
    data=csv.reader(f)
    datalist=[]
    for d in data:
        datalist.append(d)
    f.close()
    return datalist

def writecsv(filename,data_list,encode='utf-8'):
    with open(filename, 'w', newline='',encoding=encode) as f:    #newline맨뒷쪽에 백슬래시가 안들어가게 한줄단위로 저장되어 있게하는것
        csvobj = csv.writer(f, delimiter=',')
        csvobj.writerows(data_list) #여러라인을 한번에 작성할 수 있는 메소드 writerows

if __name__=='__main__':
    print('csv 읽고쓰기 파일입니다.')