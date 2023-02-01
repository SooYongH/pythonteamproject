#문자열 포맷팅
#형식1 : "문자열{위치인덱스:서식}".format(변수)
#형식2 : "문자열{변수}".format(변수=값)

name='홍길동'
age=25
print('이름: {}, 나이: {}'.format(name, age))
print('이름: {1}, 나이: {0}'.format(age, name))
print('이름: {1}, 나이: {0:3d}'.format(age, name))
#{0:n=자릿수}
print('{n}은 {a}살입니다.'.format(a=22, n='홍길동'))
print('{n}은 {a}살입니다.'.format(n='홍길동',a=22))
print('{n}은 {a}살입니다.'.format(n=name,a=age))

#range(10) = 1부터 9까지? 0부터 9까지 ㅇ