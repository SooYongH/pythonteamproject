a=[1,2,3]

try:
    print(10/0)
    print(a[4])

except IndexError as e:
    print('인덱스 범위를 벗어났어요:',e)
except ZeroDivisionError as e:
    print('0으로 나눌 수 없어요:', e) #except의 순서는 관련x/ 위에 트라이 순서로 except을 찾아서 첫번째 한 개만 실행