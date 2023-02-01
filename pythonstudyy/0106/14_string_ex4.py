# 문자열 메서드를 활용한 예제
# 문자열을 입력받아 그 중 문자 o를 $로 변경

text = input('문자열을 입력하시오')
new_text = text.replace('o', '$')
print(new_text)

# 고영선
if 'o' in text:
    print(text.replace('o', '$'))
else:
    print('문자열에 o가 없습니다.')

# 이현우
if text.find('o')>0:
    print(text.replace('o',"$"))
else:
    pass
