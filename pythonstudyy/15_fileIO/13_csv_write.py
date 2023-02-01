#csv파일 쓰기
datalist=[['id','국어','영어','수학'],
          ['1',70,80,90],
            ['2',100,90,80],['3',50,60,70]]
import csv
# f=open('data/outfile5.csv','w')
# csvobj=csv.writer(f,delimiter=',') #항목 사이마다 ,로 구분해준다
# csvobj.writerows(datalist)
# f.close()



def writecsv(filename,data_list):
    with open(filename, 'w', newline='') as f:
        csvobj = csv.writer(f, delimiter=',')
        csvobj.writerows(data_list)

writecsv('data/outfile5.csv',data_list)

#일반 txt 파일을 다룰 땐 변수=파일명.read() 형식으로 읽었는데, 12csv에선 변수=csv.reader(파일명)의 형식으로 바뀌어야 하는건가요? 서로 형식 혼용은 안되는 것이죠?