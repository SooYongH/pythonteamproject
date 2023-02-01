#파일 출력(쓰기) : write(str)
#문자열을 파일에 쓰기

'''Yesterday
All my troubles seemed so far away
Now it looks as though they're here to stay
Oh, I believe in yesterday
Suddenly
I'm not half the man I used to be
There's a shadow hanging over me
Oh, yesterday came suddenly
Why she had to go, I don't know
She wouldn't say
I said something wrong
Now I long for yesterday'''

f=open('data/outfile1.txt','w')
s=input('문자열 입력: ')
f.write(s)
f.close()

