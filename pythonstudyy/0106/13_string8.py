# 1. 대소문자 변환
# upper(), lower(), swapcase(), capitalize(), title()

s = 'i lIke pRogramming'

print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())

# 2. 문자열 검색
# count()
# find(), rfind()
# index(), rindex()
# startswith(), endswith()

s = 'i like programming, i like swimming'

# count(찾을문자열) : 찾을 문자열의 수
# count(찾을문자열, 시작위치)
# count(찾을문자열, 시작위치, 끝위치)

print(s.count('like'))
print(s.count('like',10))
print(s.count('like',10, 20))

# find(sub[, start[, end]])
#  : 찾을 문자열을 처음 만나는 인덱스
#  : 찾는 문자열이 없는 경우 -1 반환
print(s.find('like'))
print(s.find('like', 4))
print(s.find('like', 4, 25))

# rfind(sub[, start[, end]])
# : 오른쪽 부터 찾을 문자열의 위치를 반환
print(s.rfind('like'))
print(s.rfind('like', 4))
print(s.rfind('like', 4, 25))

# index(sub[, start[, end]])
# 찾을 문자열의 위치를 반환, 없는 경우 오류(비정상적으로 종료)
print(s.index('like'))
print(s.index('like', 4))
# print(s.index('like', 4, 25))

# rindex(sub[, start[, end]])
# 오른쪽에서부터 찾을 문자열의 위치를 반환, 없는 경우 오류(비정상적으로 종료)
print(s.rindex('like'))
print(s.rindex('like', 4))
# print(s.rindex('like', 4, 25))

# startswith(sub[, start[, end]])
# : 찾을 문자열로 시작하는지? 논리값으로 결과 반환

print(s)
print(s.startswith('I like'))
print(s[7:])
print(s.startswith('progr', 7))

# endswith(sub[, start[, end]])
# : 찾을 문자열로 끝나는지? 논리값으로 결과 반환

print(s.endswith('swimming'))
print(s[0:26])
print(len(s))
print(s.endswith('like', 0, 26))
print(s.endswith('like', 0, 35))


# 3. 문자열 치환 및 편집
# strip(), lstrip(), rstrip() : 공백(지정한 문자)제거
# replace() : 치환

# strip(), rstrip(), lstrip()
s = '  spam and ham   '
print(s, end='|\n')
print(s.strip(), end='|\n')
print(s.lstrip(), end='|\n')
print(s.rstrip(), end='|\n')

s = '<span><><>'
s2 = '<sp ,<an><>'
s3 = '<span><><<'
s4 = 'span><><'
s5 = 'span>><<'

print(s)
print(s.strip('<>'))
print('ㅎㅎ 파이썬'.strip('ㅎ'))
print(s2.strip('<>'))
print(s3.strip('<'))
print(s4.strip('<'))
print(s5.strip('>'))

# replace(old, new)
s = '  spam and ham   '
print(s.replace('spam', 'spam&egg'))

# expandtabs()

s = '1\tand\t2'
print(s)
print(s.expandtabs())
print(s.expandtabs(4))
print(s.expandtabs(10))

# 4. 문자열 분리와 결합
# split(), rsplit() : 분리 (공백 또는 지정한 문자열)
# join() : 결합

# split() : 하나의 문자열을 여러 문자열로 분리
s = '  spam and ham   '
t = s.split()
print(t)
print(type(t))
print(s.split('and'))

# 결합할문자열.join([여러문자열들]) : 여러 문자열들을 지정한 문자열을 사이에 넣어서 한 문자열로 결합
ch = ':'
print(ch.join(t))
print(' '.join(t))

# splitlines() : 여러줄로 되어있는 하나의 문자열을 줄단위로 문자열을 분리

s = '''first line|  
second line
third line'''
print(s)
print(s.splitlines())


# 5. 문자열 정렬
# center(width[, fillchar])
# ljust(width[, fillchar])
# rjust(width[, fillchar])

s = 'I like python'
print(len(s))
print(s.center(30), end='|\n')
print(s.ljust(30), end='|\n')
print(s.rjust(30), end='|\n')
print(s.center(30, '='), end='|\n')
print(s.ljust(30, '*'), end='|\n')

# 6. 문자열 판단
#

print('1234'.isdigit())
print('\u2155\u2156\u2159'.isnumeric())
print('love'.isalpha())
print('love123'.isalpha())
print('love123'.isalnum())
print('사랑해123'.isalnum())
print('love'.islower())
print('LOVE'.isupper())
print('This is book'.istitle())
print('\t \r\n'.isspace())
print('for'.isidentifier())

