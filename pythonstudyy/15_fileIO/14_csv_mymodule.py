import usecsv

datalist=[['id','국어','영어','수학'],
          ['1',70,80,90],
            ['2',100,90,80],['3',50,60,70]]

usecsv.writecsv('data/outfile5.csv',datalist)
#outfile5dp datalist 를 쓰고 뒤에서 여는것
data=usecsv.opencsv('data/outfile5.csv')
print(data)