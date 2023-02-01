#1. 학생별 과목들의 점수 데이터를 2차원 리스트로 생성
# 4명의 학생, 3과목(국어, 영어, 수학) 점수
# 홍길동 : 90, 85, 70
# 강감찬 : 95, 90, 70
# 이순신 : 80, 90, 90
# 유관순 : 90, 70, 70

hong = [90, 85, 70]
kang = [95, 90, 70]
lee = [80, 90, 90]
you = [90, 70, 70]

names = ['홍길동', '강감찬', '이순신', '유관순']
students = [hong, kang, lee, you]
print(students)
# students = [[90, 85, 70],[95, 90, 70],[80, 90, 90],[90, 70, 70]]

print('--#성적표(점수)--')
n = len(students)
for i in range(n):
    print(names[i], end=' : ')
    for score in students[i]:
        print(score, end=' ')
    print()

# scores=[[90,85,70],[95,90,70],[80,90,90],[90,70,70]]
# names=['홍길동','강감찬','이순신','유관순']
# n=len(names)
# for i in range(n):
#     print(names[i], end=' : ')
#     for x in scores[i]:
#         print(x,end=' ')
#     total=sum(scores[i])
#     print(f'ㅣ{total}ㅣ{total/n:.1f}')
#     print()

#2. 학생별 과목의 총점, 평균을 계산하여 과목별 점수, 총점, 평균 출력

# 출력 예시
# 홍길동 : 90 85 70 | 245 | 81.7
print('--#성적표(점수, 총점, 평균)--')
# p = len(students[0])  # 과목수
for i in range(n):
    print(names[i], end=' : ')
    total = 0
    for score in students[i]:
        print(score, end=' ')
        total += score
    print(f'| {total} | {total/len(students[i]):.1f}')
