# 다중for이용 :
# 출력결과
# 1 2 3 4
# 5 6 7 8
# 9 10 11 12

# 방법1
num = 1
for y in range(3):
    for x in range(4):
        print(num, end=' ')
        num += 1
    print()

# 방법2
for y in range(3):
    for x in range(1, 5):
        print(x+4*y, end=' ')
    print()

# 김현우
# for y in range(1):
for x in range(1,13):
    print(x, end=' ')
    if x % 4 == 0:
        print()
