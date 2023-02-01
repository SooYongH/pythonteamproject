# 날짜형식 변경
# 입력한 날짜를 10년 뒤 날짜를 계산하여 출력
# 입력 날짜 형식은 2023/01/06
# 출력 날짜 형식은 2033년 1월 6일

cur_date = input('날짜(년/월/일) 입력: ')
print(f'입력날짜는 {cur_date}')
item = cur_date.split('/')
year = int(item[0])+10
month = item[1]
day = item[2]

new_date = str(year) +'년'+ month + '월' + day +'일'
print(new_date)