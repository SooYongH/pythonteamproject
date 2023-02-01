# 예제_문자열의 각 문자 뒤에 특수문자($) 붙이기

# strs='파이썬짱?'
# for s in strs :
#     print(s, end='$')
#     # strs 변수의 문자열을 하나씩 인식을 하는거야
#
# strs='파이썬짱?'
# res=''
# for s in strs :
#     res=res+s+'$'
# print(res)
# 프린트하고 끝이 아니라 데이터를 만들어서 계속해서 활용하고 싶으니 res라는 변수에 값을 계속 저장한거야

#예제_출력결과 : '파#썬#재#있#요#
# s2='파이썬은재미있어요'
#
# res=''
# for s in s2[::2]:
#     res=res+s+'#'
# print(res)

#요 뒤에 # 안나오게 하고 싶어
# for i in range(len(s2)) :
#     if i%2==0 :
#         res=res+s2[i]
#     else:
#         res=res+'#'
# print(res)

#예제_s2 거꾸로 출력하기

#방법1
# s=input('문자열을 입력하세요 : ')
# print(s[::-1])

#방법2
# s=input('문자열을 입력하세요 : ')
# n=len(s)
# res=''
# for i in range(n) :
#     print(s[n-1-i], end='')
#     res+=s[n-1-i]

#방법3
s=input('문자열을 입력하세요 : ')
n=len(s)
res=''
for i in range(n-1,-1,-1):
    #range(시작num,끝num,-1=거꾸로해라)
    #시작num > 끝num 도 돼
    #(n-1,0,-1) 하면 안됨 0의 자리까지 하고 싶은데 range는 끝넘버 미만 그 전까지로 범위를 한정하기에 0-1=-1해야됨
    print(s[i],end='')
    res+=s[i]
print()
print(res)


