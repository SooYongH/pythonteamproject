#클래스변수와 인스턴스변수

class Car:
    count=0

    def __init__(self,color,speed=0):
        self.color=color #인스턴스 변수
        self.speed=speed #인스턴스 변수
        Car.count+=1 #반드시 클래스 변수 'Car'를 써야만 공유가 됨
        print(f'현재 {Car.count}번째 자동차가 출시되었습니다')

car1=Car('White')
car2=Car('Black')
car3=Car('Blue')

print('car1',car1.count)
print('car2',car2.count)
print('car3',car3.count)

print(id(car1.count))
print(id(car2.count))
print(id(car3.count)) #클래스 변수는 모든 인스턴스가 공유

print('car1 color', id(car1.color))
print('car2 color', id(car2.color))
print('car3 color', id(car3.color))

car1.count=100
print(car2.count)
print(id(car1.count)) #주소 바껴서 공유안됨/클래스 안에서 관련 메서드를 만들어줘야 함께 공유할 수 있음
print(id(car2.count))
print(id(car3.count))

print(Car.count)
Car.count=100 #밖에서 공유하려면 클래스 변수를 사용해야함
print(car1.count)
print(car2.count)
print(car3.count)