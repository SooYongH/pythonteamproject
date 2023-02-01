# 리스트 컴프리헨션
# 순차적인 리스트를 한 줄의 코드로 생성
# 형식 : 리스트명 = [수식 for 항목 in range() if 조건식   ]

# 1~5까지 숫자 리스트 생성

numList = []
for num in range(1, 6):
    numList.append(num)
print(numList)

# 컴프리헨션으로 수정
numList = [num for num in range(1, 6)]
print(numList)

numList2 = [num*2 for num in range(1, 6)]
print(numList2)

numList3 = [num for num in range(1, 6) if num%2==0]
print(numList3)

numList4 = [num**2 for num in range(1, 6)]
print(numList4)

# 3의 배수
numList5 = [num for num in range(3, 20, 3)]
print(numList5)

numList6 = [num for num in range(1, 20) if num%3==0 ]
print(numList6)