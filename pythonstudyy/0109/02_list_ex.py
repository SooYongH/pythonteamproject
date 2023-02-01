#리스트와 반복문을 사용하여 10개의 정수 입력받아 합계와 평균 구하기

data=[]
for i in range(1,11):
    data.append(int(input(f'{i}번째 정수를 입력하세요.')))
total=0
for i in range(10):
    total+=data[i]
aver=total/len(data)

print(f'합계는 {total}, 평균은 {aver}입니다.')

#압축버전
data=[]
total=0
for i in range(1,11):
    data.append(int(input(f'{i}번째 정수를 입력하세요.')))
    total+=data[i-1]
aver=total/len(data)
print(f'합계는 {total}, 평균은 {aver}입니다.')

# data라는 리스트 요소(10개) 출력
# for i in range(10):
#     print(data[i])
#리스트 대괄호는 data[0]:첫 번째 요소 / data[-1]:뒤에서 첫번째 요소(마지막 요소)

# for x in data:
    # print(x)

#b=[1,2,3,[10,20]]
# b[-1][0] : 맨 마지막의 첫번째 요소