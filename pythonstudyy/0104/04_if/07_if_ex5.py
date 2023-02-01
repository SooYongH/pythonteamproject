# 도형을 선택하면 넓이를 구하기 위한 값을 입력받아 면적 구하기
# 김태효
'''
figure = int(input('도형입력(1: 사각형, 2: 삼각형, 3: 원): '))

if figure == 1:
    h = int(input('가로 입력: '))
    v = int(input('세로 입력: '))
    print(f'사각형의 면적 = {h * v}')
elif figure == 2:
    h = int(input('밑변 입력: '))
    v = int(input('높이 입력: '))
    print(f'삼각형의 면적 = {0.5 * h * v}')
else:
    r = int(input('반지름 입력: '))
    print(f'원의 면적 = {2 * 3.14 * r}')

# 최진영
shape = input('도형 입력 (1 : 사각형, 2 : 삼각형, 3 : 원) : ')
if shape == '1' :
    x1 = float(input('가로 입력 : '))
    y1 = float(input('세로 입력 : '))
    print(f'사각형의 면적 = {x1 * y1}')
elif shape == '2' :
    x2 = float(input('밑변 입력 : '))
    y2 = float(input('높이 입력 : '))
    print(f'삼각형의 면적 = {x2 * y2/2}')
elif shape == '3' :
    r = float(input('반지름 입력 : '))
    print(f'원의 면적 = {3.14 * r **2}')
else :
    print('도형 입력을 잘못하셨습니다.')

'''
# 정다운
shape = int(input("넓이를 구할 도형을 선택하시오. 1.rec / 2.tri / 3.cir"))
if shape == 1 :
    print("1. 사각형을 선택하셨습니다. ")
    w = int(input('넓이를 입력하시오 : '))
    h = int(input('높이를 입력하시오 : '))
    print(f'면적은 {w*h}입니다.')
elif shape == 2 :
    print("2. 삼각형을 선택하셨습니다.")
    b = int(input("밑변을 입력하시오 : "))
    h = int(input('높이를 입력하시오 : '))
    print(f'면적은 {b * h *0.5}입니다.')
elif shape  == 3:
    print("3. 원을 선택하셨습니다.")
    r = int(input("반지름을 입력하시오 : "))
    print(f'반지름 {r}인 원의 면적은 {r**2*3.14 :.2f} 입니다')
else :
    pass



