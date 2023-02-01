#upper(), lower(), swapcase(), capitalize(), title()

s='I like programming, i like swimming'

print(s.upper())
#다 대문자
print(s.lower())
#다 소문자
print(s.capitalize())
#첫글자만 대문자 나머지 소문자
print(s.title())
#각 단어의 첫 글자를 모두 대문자로
print(s.swapcase())
#대문자는 소문자로 소문자는 대문자로 교환

#문자열 검색
print(s.count('like'))
print(s.count('like',10))
#10이후부터 like가 몇개인지
print(s.count('like',10,20))
#10부터 20까지(범위) like가 몇개인지
print('count와 find')
print(s.find('like'))
#어디에 몇번째에 있어
print(s.find('like',4))
#4이후 몇번째에 있어
print(s.find('like',4,25))
#-1= 없다

#rfind() : 오른쪽 끝부터 찾을 문자열의 위치를 반환 / 형식 똑같
print(s.rfind('like'))
print(s.rfind('like',4,))
print(s.rfind('like',4,25))

# #index() : find랑 똑같은 형식, 결과 / 찾는게 없으면 값을 출력하지 않으면서 exit code 1
# # 그래서 index보다 find를 사용
# print(s.index('like'))
# print(s.index('like',4,))
# print(s.index('like',4,25))

#rindex() : rfind()와 비슷/ 없으면 에러코드

#startswith(sub,start,end) : 찾을 문자열로 시작하는지?
#논리값 bool(True/False)로 답변
print(s[7:])
print(s.startswith('i like'))

#endswith() : 찾을 문자열로 끝나는지?
print(s[0:26])
print(s.endswith('i like',0,26))

#strip(), lstrip()왼쪽 정렬, rstrip()오른쪽 정렬 : 공백(지정한 문자) 제거
#replace() : 치환
s='    spam and ham   '
print(s)
print(s.strip(),end='ㅣ\n')
print(s.lstrip(),end='ㅣ\n')
print(s.rstrip(),end='ㅣ\n')

s='<spam><><>'
print(s)
print(s.strip('<>'))
print('ㅎㅎ파이썬'.strip('ㅎ'))

#replace('이거를', '요걸로바꿔')
print(s.replace('spam','spam&egg'))

#expandtabs()
s='1\tand\t2'
#\t:탭을 해라/
print(s)
print(s.expandtabs())

#문자열 분리와 결합
#split(), rsplit() : 분리(공백 또는 지정한 문자열)

s='   spam and ham   '
print(s.split())
#공백 기준으로 리스트로 자르는것
print(s.split('and'))
#'and' 기준으로 앞뒤 자름

#join() : 지정한 문자열을 여러 문자열들 사이에 넣어서 한 문자열로 결합
ch=':'
t=s.split()
print(ch.join(t))

#splitlines() : 여러 줄로 되어있는 하나의 문자열을 줄단위로 문자열을 분리

#문자열 정렬 : center(), ljust(), rjust()
s='l like python'
print(len(s))
print(s.ljust(30), end='\n')
#30자로 지정
print(s.center(30,'='), end='\n')

#문자열 판단
print('1234'.isdigit())
print('\u2155\u2156'.isdigit())
# 특수기호마다 각 코드가 있음 /
# isdigit() : 정수
# isnumeric() : 숫자
#isalpha():문자열이냐(한글도 ㅇ)
#isalnum() : 문자열+숫자냐
#isupper() : 대문자
#islower() : th문자
print('\t \r\n'.isspace())
print('for'.isidentifier())
print('This is book'.istitle())
