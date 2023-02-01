# 구구단 출력(2~9단)

# for dan in range(2, 10):
#     for num in range(1, 10):
#         print(f'{dan}*{num}={dan*num:2d}')
#     print()

# 권예진
for dan in range(2, 10) :
    print(f'{dan}단을 외우자!  ', end = " ")
print ()
for y in range(1, 10) :
    for x in range(2,10) :
        print(f'{x} * {y} = {y*x:2d}', end = '  | ')
    print()
