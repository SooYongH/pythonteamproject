# 5명의 학생의 점수에 대해 합격/불합격 출력
# 60점이상이 합격
# data = [90, 57, 88, 40, 78]

# 출력예시
# 1번 90점 합격
# 2번 57점 불합격

#강대영
datum = [90,57, 88, 40, 78]
id = 1
# for data in datum :
#     if data>=60:
#         print(f'{id}번 {data}점 합격')
#     else:
#         print(f'{id}번 {data}점 불합격')
#     id = id+ 1

# Tip
res = ''
for data in datum :
    res = '합격' if data>=60 else '불합격'
    print(f'{id}번 {data}점 {res}')
    id = id+ 1