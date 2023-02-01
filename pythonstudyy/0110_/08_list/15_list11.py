# 2차원리스트
# 1차원 리스트를 여러 개 연결한 것처럼

num_list = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(num_list)
print(num_list[0])
print(len(num_list[0]))
print(num_list[0][3])

# 2차원 리스트의 요소를 출력
for x in num_list:
    print(x)

for x in num_list:
    for y in x:
        print(y, end=' ')
    print()

# 황윤서
r = len(num_list)
c = len(num_list[0])
print(f'{r}행{c}열')
for j in range(r):
    for i in range(c):
        print(num_list[j][i],end=' ')
    print()


# 불규칙한 2차원 리스트

num_list2 = [[1,2,3,4],[5,6],[7,8,9]]
print(num_list2)

for x in num_list2:
    for y in x:
        print(y, end=' ')
    print()