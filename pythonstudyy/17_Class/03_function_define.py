#메서드 정의
class Car:
    color=''
    speed=0

    def drive(self,speed): #self_인스턴스가 생성됐을 때 자신의 것이라는 것을 지칭하기 위한 변수 / 매개변수 주는 값(인수) 필요없음
        self.speed=30
        print('주행하다')

car1=Car()
print('drive()수행전: speed=', car1.speed)
car1.drive()
print('drive()수행후 speed=', car1.speed)
