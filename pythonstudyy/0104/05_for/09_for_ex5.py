# 삼각형 모양 출력하기

for i in range(1,6):
    for j in range(i):
        print('*', end=' ')
    print()

for i in range(5,0,-1):
    for j in range(i):
        print('*', end=' ')
    print()


for i in range(1,6):
    print('*'*i)

for i in range(5,0,-1):
    print('*'*i)