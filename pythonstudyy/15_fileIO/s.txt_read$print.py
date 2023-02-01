with open('data/s.txt','r') as f:
    data=f.readlines()
# print(data)
# print(sorted(data))
outdata=sorted(data)

with open('data/s.out','w') as f2:
    f2.writelines(outdata)