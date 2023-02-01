# 내장함수들

print(' chr(정수) : ASCII코드 문자 반환')
print(chr(65))
print(chr(90))
print(chr(100))
print(chr(124))
print(chr(35))

print(' ord(문자) : ASCII코드 숫자 반환')
print(ord('a'))
print(ord('$'))
print(ord('+'))

print('any(iterabel) :논리값 반환')
print(any([-4, -10, 49, 4.5]))
print(any([-4, 0, 49, 4.5]))
print('all(iterabel) :논리값 반환')
print(all([-4, -10, 49, 4.5]))
print(all(['345', 10, [1,2], 4.5, (1,2)]))
print(all(['123', 10, [], 4.5, (1,2)]))

print('min(iterabel) :최소값을 반환')
print(min([-4, -10, 49, 4.5]))
print('max(iterabel) :최대값을 반환')
print(max([-4, -10, 49, 4.5]))
print('sum(iterabel) :합을 반환')
print(sum([-4, -10, 49, 4.5]))

print('pow(x,y) : x의 y거듭제곱 반환')
print(pow(3,8))

print('divmod(a,b): a를 b로 나눈 몫과 나머지를 튜플형식으로 반환')
print(divmod(9,2))

print('round(num[, ndigits]): 실수를 반올림')
print(round(3.14))
print(round(3.141592, 3))

print('enumerate() : 시퀀스 데이터를 인덱스값을 포함하여 enumerate객체로 반환')
print(list(enumerate(['a','b','c'])))
# [(0, 'a'), (1, 'b'), (2, 'c')]
for i, v in enumerate(['a','b','c']):
    print(i+1, v)

print('eval(표현식): 표현식의 연산결과 반환')
print(eval('1+3'))
print(eval('1'+'3'))

print('filter(함수, 데이터): iterable 데이터에 함수를 적용하여 데이터를 걸러냄')
print(list(filter(lambda x: x>0, [-10, 0, -4, 10, 7])))
def minus(x):
    return x<0
print(list(filter(minus, [-10, 0, -4, 10, 7])))

# enumerate()
# map()
# zip()
# filter()

print('help() : 도움말 페이지')
help(sum)
help(filter)

# 진법변환 : bin(), oct(), hex()
# 문자를 숫자로변환 : int(), float()
# 숫자를 문자변환 : str()

# 표준입출력함수 : input(), print()
# 데이터 유형확인 : type()
# 변수,객체 메모리 주소 :id()
# 자료구조생성, 변환 : list(), tuple(), dict(), set()
# 지정하는 범위값 생성 : range()
# 시퀀스(sequence) 또는 컬렉션(collection) 데이터 길이 반환 : len()
# 객체(변수) 또는 객체의 요소 삭제 : del()

# 정렬 : sorted(iterable, reverse=True, key=None) -> 원본복사 새로운 정렬데이터 반환
print('sorted(): ')
print(sorted('I am a girl!'))
print(sorted('I am a girl!', reverse=True))
print(sorted('I am a girl!', key=str.lower))

# open() : 파일입출력 함수 (뒤에 설명)
