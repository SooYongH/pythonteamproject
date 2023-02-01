#예외처리문 : try~except

try:
    print(10/0)
#     print('나이:'+23+'살')
except :
    print('emergency!')

try:
    print(10/0)
#     print('나이:'+23+'살')
except ZeroDivisionError:
    print('0으로 나눌 수 없습니다.')

try:
        # print(10 / 0)
    print('나이:'+23+'살')
except TypeError:
    print('타입이 통일되지 않았습니다')

try:
        # print(10 / 0)
    print('나이:'+23+'살')
except TypeError as e: #해결방법 메시지 받아서 붙여넣기/e=에러 메시지변수
    print('타입이 통일되지 않았습니다',e)

