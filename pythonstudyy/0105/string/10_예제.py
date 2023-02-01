# str = input('문자열을 입력하세요: ')
# res = str.replace('o', '$')
#
# print('결과 출력:', res)
#

#날짜 형식 변경
#입력한 날짜를 10년 뒤 날짜를 계산하여 출력
#입력 날짜 형식은 2023/01/06
#출력 날짜 형식은 2023년1월1일

date=input('날짜(년/월/일) 입력하세요')
print(f'입력날짜는{date}')
b=date.split('/')
year=int(b[0]) +10
month=b[1]
day=b[2]
new_date=str(year)+'년'+month+'월'+day+'일'
print(new_date)
