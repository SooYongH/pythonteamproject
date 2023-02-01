class Car:
    def __init__(self,color,speed):
        self.color=color
        self.speed=speed

    def drice(self):
        print(f'{self.speed}로 주행합니다')

class Truck(Car):
    def __init__(self,color,speed,load):
        super().__init__(color.speed)
        self.load=load

    def drive(self):
        print(f'{self.speed}로 {self.load}양의 짐을 싣고 주행합니다')

    def loading(self):
        print(f'현재 적재량은 {self.load}입니다')