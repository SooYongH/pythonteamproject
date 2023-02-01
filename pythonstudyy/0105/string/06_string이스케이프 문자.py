#다양한 문자열 표현가 이스케이프 문자 (\t, \\,\', \", \n)

# s1= 'yes,it is.'
# s2= "it's not you..."
# s3= 'He said, "Yes i am."'
s4= 'Don\'t walk.'

#여러줄로 작성했으나, 한 줄 문자열로 표현하고자 할때 : 줄 마지막에 \ 삽입
s5='yes,it is.\
it\'s not you...\
He said, "Yes i am."'

print(s4,s5)

#여러줄 문자열: ''' ''', """ """