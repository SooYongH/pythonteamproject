# 형변환 함수 : str(), int(), float()

name = 'kim'
age = '25'
address = 'Seoul'
# print(type(age))
# print(int(age))
# print(type(int(age)))

print(f'당신의 나이는 {int(age)+1}이군요')

# int(문자열, 진수)
print(int('ff', 16))
print(int('123', 16))
print(int('123', 8))
print(int('1101', 2))
print(int('12345', 10))

# float(문자열)
print(float('10.345'))

