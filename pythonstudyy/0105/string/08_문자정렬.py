#문자열 정렬 서식
# 왼쪽정렬 : <
# 오른쪽정렬 : >
# 가운데정렬 : ^
# 공백문자 지정 : -

# s='python'
# print('{:<10}'.format(s))
# {:<10}={0:0<10}=처음부터 끝까지 10칸 확보하여 왼쪽정렬
# print('{:>10}'.format(s), end='!')
# print()
# print('{:^10}'.format(s), end='!')
# print()
# print('{:#^10}'.format(s), end='!')

first_value = 0
second_value = 0
for i in range(1, 10):
    if i is 5:
        continue
        first_value = i
    if i is 10:
        break
    second_value = i
print(first_value + second_value)