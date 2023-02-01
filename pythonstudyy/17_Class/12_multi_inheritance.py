#다중상속

class Person:
    name=''
    age=0

    def greeting(self):
        print('안녕하세요!')

class University:
    department=''
    grade=1

    def manageScore(self):
        print('학점관리')

    def greeting(self):
        print('안녕 난 그리팅 중!')

class Undergraduate(Person, University):
    def study(self):
        print('공부하기')

kim= Undergraduate()
kim.greeting() # 자신(Undergraduate), 왼(Person), 오(University)순으로 상속 진행 / 그래서 Person의 안녕하세요를 출력
kim.manageScore()
kim.study()
print(Undergraduate.mro()) #다중상속의 순서를 알려주는 메소드
