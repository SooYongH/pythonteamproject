#리스트 역순으로 출력하기
# 0이상 100이하의 짝수를 갖는 리스트를 생성한다
data=[]
for i in range(0,101,2):
    #  range(0,101)하고   if i%2==0 :
    #                        data.append(i)
    data.append(i)
print(data)
# print(len(data))

# 1번에서 생성한 리스트의 값을 역순으로 갖는 리스트를 생성한다.
r_data=[]
for x in range(len(data)-1, -1,-1):
    #첫째자리인 0까지 출력하려면 -1하여 -1로 범위를 줘야함
    r_data.append(data[x])
print(r_data)

print(r_data[::-1])