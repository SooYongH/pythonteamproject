#특별한 메서드 정의

class Line:
    length=0

    # 생성자
    def __init__(self,length):
        self.length=length

    #소멸자 : del()
    def __del__(self):
        print(self.length,'길이의 선분이 삭제되었습니다.')
    #시키는거 끝나면 종료하고 삭제해버림

    def __repr__(self):
        return f'선분의 길이가 {self.length}인 Line인스턴스입니다.'
    #__str__():
    #이것도 객체가 가지고 있는 정보를 출력

    def __add__(self, other):
        return self.length + other.length

    def __sub__(self, other):
        return self.length - other.length

    def __mul__(self, other):
        return self.length * other.length

    def __lt__(self, other):
        return self.length < other.length #정수값 전제하에 비교연산 가능

    def __gt__(self, other):
        return self.length > other.length

    def __eq__(self, other):
        return self.length == other.length

    def __ge__(self, other):
        return self.length >= other.length

   #divmod(x=나눈 몫,y=나눈 나머지)
    def __divmod__(self, other):
        return self.length // other.length, self.length % other.length


line1=Line(100)
line2=Line(200)

print(line1)
print(line1+line2)
print(line1-line2)
print(line1*line2)

if line1 > line2:
    print('line1이 더 크네요')
elif line1==line2:
    print('두 선분 길이가 같아요')
else:
    print('line2가 더 긴가요?')

print(divmod(line1,line2))