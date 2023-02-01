# 문제. 사각형의 가로와 세로길이를 입력받아 면적계산하고 반환하는 함수 get_area() 정의

# 가로길이 입력 : 10
# 세로길이 입력 : 20
# 사각형의 면적 = 200

def get_area():
    width = int(input('가로길이입력 :'))
    height = int(input('세로길이입력 :'))
    print('사각형의 면적 %d' % (width * height))

# get_area()

def get_area2():
    width = int(input('가로길이입력 :'))
    height = int(input('세로길이입력 :'))
    return width * height

print('사각형의 면적 %d' % (get_area2()))


