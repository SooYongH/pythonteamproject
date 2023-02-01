#메서드 정의
class Car:
    color=''
    speed=0

    # def drive(self,speed): #스피드를 바꿔주고 싶어
    #     self.speed=speed #셀프 스피드라는 필드에 내가 정한 값 스피드를 저장(speed(필드)!=speed(매개변수)
    #     print('f{self.speed}로 주행하다')

    def drive(self,speed=30): #디폴트 기본값 지정
        self.speed=speed #셀프 스피드라는 필드에 내가 정한 값 스피드를 저장(speed!=speed)
        print(f'{self.speed}로 주행하다')

car1=Car()
print('drive()수행전: speed=', car1.speed)
car1.drive() #디폴트값
car1.drive(50) #지정인수
print('drive()수행후 speed=', car1.speed)


