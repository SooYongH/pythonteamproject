#생성자(constructor) : 인스턴스를 생성하면서 클래스에서 사용할 필드 값을 지정하고 초기화시키는 함수
#생성자 기본 형식 :
# def __init__(self,*args):
#     self.color='red'
#     self.speed=0 필드 생성 및 설정

class Car:
    # def __init__(self):
    #     self.color='black'
    #     self.speed=0
    #
    def __init__(self,model, color='black',speed=0): #위치인수가 키워드 인수보다 더 앞으로 나와함
        self.model = model
        self.color=color
        self.speed=speed

    def drive(self,speed=30):
        self.speed = speed
        print(f'{self.speed}로 주행하다')

car1=Car('Genesis') #디폴트
car2=Car('BMW','red',70) #커스터마이징
car3=Car('Nexo','yello')

print(f'자동차1의 모델명은 {car1.model}')
print(f'자동차2의 스피드는 {car2.speed}')
print(f'자동차3의 컬러는 {car2.color}')

car2.drive()



