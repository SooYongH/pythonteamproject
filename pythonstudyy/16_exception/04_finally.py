#try~except~else~finally
 # else fianlly 생략가능

try:
    f=open('exception.txt','r')
except FileNotFoundError :
    pass
else:
    data=f.read()
    print(data)
    f.close()
finally:  #정상작동이든, 오류발생이든 항상 실행
    print('종료')