# 세 과목의 점수에 대하여 총점과 평균을 계산하고 출력하기

kor = 90
math = 80
eng = 80
# 총점 = 250, 평균 = 83.33

# print(' 총점 = %d,'%(kor+eng+math),'평균 = %.2f'%((kor+eng+math)/3))

# total=kor+eng+math
# print("총점: {}, 평균: {:.2f}".format(total,total/3))

# 총점 = kor + math + eng
# 평균 = (총점 / 3)
#
# print('총점:{}, 평균:{:.2f}'.format(총점,평균))


sum = kor + eng + math
avg = sum / 3

print('총점 = %d, 평균 = %f' %(sum, avg))
print('총점 = {}, 평균 = {:.2f}'.format(sum, avg))

