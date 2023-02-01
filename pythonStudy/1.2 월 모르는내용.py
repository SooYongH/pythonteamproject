print('성명 : %s, 학번 : %s, 학년 : %d, 평균 : %10.2f 입니다.' % (name, 학번, 학년, 평균))
성명 : 황수용, 학번 : 2018018359, 학년 : 4, 평균 :       4.12 입니다.
print('성명 : %s, 학번 : %s, 학년 : %d, 평균 : %0.2f 입니다.' % (name, 학번, 학년, 평균))
성명 : 황수용, 학번 : 2018018359, 학년 : 4, 평균 : 4.12 입니다.
print('성명 : %s, 학번 : %s, 학년 : %d, 평균 : %.2f 입니다.'%(name, 학번, 학년, 평균))
성명 : 황수용, 학번 : 2018018359, 학년 : 4, 평균 : 4.12 입니다.

format(1.234567,'.3f')
'1.235'
'name={}, age={}'.format('이순신',33)
'name=이순신, age=33'

kor=90
math=80
eng=80

total=kor+math+eng
aver=total/3

print('총점={1:3d}, 평균={0:.1f}'.format(aver,total))
총점=250, 평균=83.3

a=300
b=0b1010
c=0o123
d=0xa9f

print(a,b,c,d)
300 10 83 2719
#모두 10진수로 프린팅

#escape문자 백스페이스\ 
word = "doesn't"
word2= 'doesn\'t'
print(word, word2)
doesn't doesn't
word3= "He said \"yes\""
print(word3)
He said "yes"
print('안녕\n하세요', '안녕\t하세요', '안녕\t\t하세요')
안녕
하세요 안녕	하세요 안녕		하세요
#escape문자 r 
path = 'c:\info\name'
path2 = r'c:\info\name'
print(path,path2)
SyntaxError: multiple statements found while compiling a single statement

#escape문자 ; 여러 문장을 한 줄에 사용 
a=10; b=40; c=50; d='hi'
print(a,b,c,d)
10 40 50 hi

print('first');print('second')
first
second
print('first',end='');print('second')
firstsecond
print('first',end='-');print('second')
first-second

#fstring
print(f'이름은 {name}, 나이는 {age:.1f}에요.')
이름은 황수용, 나이는 25.0에요.
age=print(input('나이는?,end=()'))
print('당신의 나이는,str(age)+'군요!')

#eval 숫자(정수, 실수 구분가능)로 형변환해
