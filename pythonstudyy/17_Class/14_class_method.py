#클래스 메서드 : 클래스 변수나 클래스 메서드 사용할 때
#@classmethod 키워드를 메서드 앞에 붙임

class Person:
    count=0

    def __init__(self):
        Person.count+=1  #count : 클래스 변수

    @classmethod
    def print_count(cls): #self 대신 cls 써야함
        print(f'{cls.count}명 태어났어요')

kim=Person()
lee=Person()
Choi=Person()

Person.print_count()