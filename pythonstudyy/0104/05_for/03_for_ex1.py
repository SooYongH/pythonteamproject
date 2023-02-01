# 1에서 100까지의 합 구하기
total = 0
for num in range(1, 101):
    total += num
print(f'1~100까지의 합은 {total}')

# 1에서 20까지의 정수 중 3의 배수 출력
total = 0
for num in range(3, 20, 3):
    total += num
print(f'1~20까지의 정수 중 3의 배수의 합은 {total}')

# for와 if문을 함께 사용: 3의 배수의 합
total = 0
for num in range(1, 20):
    if num % 3 == 0:
        total += num

print(f'1~20까지의 정수 중 3의 배수의 합은 {total}')


# 최원준
for tri in range(1,21):
    if tri % 3 == 0:
        print(tri)

#
# 이동훈
# for num2 in range(1, 10):
#     print(sum(num2))

# Tip. sum()함수
data = list(range(1,101))
type(data)
sum(data)