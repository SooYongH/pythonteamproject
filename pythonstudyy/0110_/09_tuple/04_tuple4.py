# 튜플의 덧셈, 곱셈

t1 = (1,2,3,4)
t2 = ('a', 'b', 'c', 'd')
print(t1+t2)
print(t1*3)

# 2차원 튜플
t3 = (1,2,3), (4,5,6), (7,8,9)
print(t3)

for x in t3:
    for y in x:
        print(y, end=' ')
    print()