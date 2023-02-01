name = '홍길동'
age = 18
address = '강남구'

print(name, age)
print(name, '은', address, '에 산다')
print(name+'은', address+'에 산다')



# 파이참의 단축키
# 파일 저장 : Ctrl + S
# 편집시 - 한줄 삭제 : Ctrl + x
#       - 복사 : Ctrl + c  -> Ctrl +v
# 주석만들기 : Ctrl + /
# 실행(Run) : Shift+F10  Alt+Shift+F10
# 실행 취소  : Ctrl+Z

# print()
# id()
# type()

# error 유형1
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.1\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# NameError: name 'a' is not defined

# 문자열과 숫자는 + 연산자 사용할 수 없음
10 + '살'


# error 유형2
# Traceback (most recent call last):
#   File "C:\Program Files\JetBrains\PyCharm Community Edition 2022.3.1\plugins\python-ce\helpers\pydev\pydevconsole.py", line 364, in runcode
#     coro = func()
#            ^^^^^^
#   File "<input>", line 1, in <module>
# TypeError: unsupported operand type(s) for +: 'int' and 'str'