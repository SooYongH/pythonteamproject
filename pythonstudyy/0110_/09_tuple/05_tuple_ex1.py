# 튜플에 데이터 40을 추가할 수 있는 방법은?
t1 = (10, 20, 30)

# 방법1 . 40이 저장된 새로운 튜플과 + 연산
t2 = 40,
#t2타입은 int 숫자 여러개 나열이면 튜플인데 정수 하나이기 때문에 int
#이때는 콤마를 무조건 써야 함 t2=(40,) 또는 t2=40,
print(type(t2))
# print(t1+t2)
t1 = t1 + t2
print(t1)

# 방법2. 리스트로 변환한 뒤 40을 추가하고 튜플로 변경
# t1 = list(t1)
# t1.append(40)
# t1 = tuple(t1)
print(t1)