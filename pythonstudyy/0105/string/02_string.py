# 문자열 슬라이싱
# 문자열의 일부분을 가져오기
# 형식 : [start:end] 출력은 end-1까지
# 형식 : [start:end:step] 숫자 생략 -> 처음 or 끝 의미

s='abcdefghijk'
print(s[1:3])
print(s[:3])
print(s[3:])
print(s[3:])
print(s[2:5:2])
print(s[2::2])
print(s[:])
print(s[::-1])
print(s[::-2])