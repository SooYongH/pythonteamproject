# 각 정보를 갖는 변수들을 이용하여 예시와 같이 출력하기
# name, no, year, grade, average
# 문자열 : 문자의 나열 (한개 이상의 문자들)

name = '홍길동'
no = '2016001'
year = 4
grade = 'A'
average = 93.5
# print('성명 : ' + name)
# print('학번 : ' + no)
# print('학년 : ' + str(year) )
# print('학점 : ' + grade)
# print('평균 : ' + str(average) )

# print('성명 :' , name)
# print('학번 :' , no)
# print('학년 :' , year)
# print('학점 :' , grade)
# print('평균 :' , average)

print('성명 : ' + name)
print('학번 : ' + no)
print('학년 :' , year)
print('학점 : ' + grade)
print('평균 :' , average)

# 포맷코드를 사용하여 출력하기
print('성명 : %s \n학번 : %s \n학년 : %d \n학점 : %c \n평균 : %f' % (name, no, year, grade, average))
print('----------------')

print('성명 : %s' % name)
print('학번 : %s' % no)
print('학년 : %5d' % year)
print('학점 : %s' % grade)
print('평균 : %10.1f' % average)


