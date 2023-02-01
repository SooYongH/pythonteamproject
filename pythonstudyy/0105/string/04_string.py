#in/not in 연산자
#결과는 True / False

s='Python Programming'
print('python' in s)
print('Py' in s)
print(' P' in s)

s2='Python'
if s2 not in s:
    print('없어')
else :
    print('있어')
