# 예제. 1~10까지의 정수들의 합계를 구하고 출력하기

total = 0   # 변수 초기화
for num in range(1,11):
    # print(num)
    total = total + num
    print(f'num={num}')
    print(f'total={total}')
print(total)

# 주의: 더한 결과를 저장하는 변수의 값을 초기화하지 않는 경우 NameError 발생