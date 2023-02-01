# 행분리 ( \ )
# 한줄로 다 표현하지 않는 경우 여러줄로 쓰지만 한줄로 인식
a, b, c, d, e, f, g = 10, 12, 12, 34, 12, 34, 50

total = a + b + c +d + \
+ e + f
print(total)

# print()함수에서 여러행으로 입력하나 하나의 행으로 출력
print('긴문장을 입력할 때'
      '두번째 줄의 내용'
      '세번쨰....')

# print()에서 한줄 입력을 여러줄로 출력 :  \n (Escape문자)
print('긴문장을 입력할 때\n'
      '두번째 줄의 내용\n'
      '세번쨰....')


# Escape문자 : \n , \t, \\, \', \"
print('안녕\n하세요')
print('\t안녕\t\t하세요')
print('안녕\\now')

word = "doesn't"
word2 = 'doesn\'t'
print(word, word2)
word3 = "He said \"yes\""
print(word3)

# escape 문자로 인식하지 않고 문자열 그대로 인식 변경 : r추가 (raw)
# path = 'c:\info\name'
path2 = r'c:\info\name'
print(path2)


# 행결합 : 여러 문장을 한 줄에 사용
a = 10; b = 40; c = 50; d = 'hi'



