import csv

with open('data/s.txt.csv','r',encoding='utf-8') as f:
    data=csv.reader(f)
    print(data)