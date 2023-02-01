#비공개 메서드와 비공개 필드

class Car:
    def __init__(self, model, color='black', speed=0):  # 위치인수가 키워드 인수보다 더 앞으로 나와함
        self.model = model
        self.__color = color  #비공개필드
        self.speed = speed

    def drive(self, speed=30):
        self.speed = speed
        print(f'{self.speed}로 주행하다')

#비공개 메서드는 바로 사용(출력) 불가/ 따라서 반환 가능케하는 메서드 생성
    def getColor(self):
        return self.__color

    def __getModel(self):
        return self.model

# 비공개 메서드는 지정도 불가/ 따라서 접근 가능케하는 메서드 생성
    def setColor(self,color):
        self.__color=color

    def setModel(self,model):
        self.model=model

    def printInfo(self):
        print('모델명은',self.__getModel())
        print('컬러는', self.getColor())

myCar=Car('bmw')
myCar.setColor('red')
# print(myCar.__color) #접근불가
print(myCar.getColor())

print(myCar.model)
# print('색상은', myCar.__getModel()) #접근불가