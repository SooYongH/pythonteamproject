# zip() : 두 리스트를 조합

names = ['kim', 'hong', 'lee', 'choi']
foods = ['오뎅', '라면', '순대국', '파스타', '피자']
drinks = ['사이다', '콜라', '커피', '홍차']

print(list(zip(names, foods, drinks)))
for x, y, z in zip(names, foods, drinks):
    print(x, y, z)

# for x, y in [('kim', '오뎅'), ('hong', '라면'), ('lee', '순대국'), ('choi', '파스타')]:
