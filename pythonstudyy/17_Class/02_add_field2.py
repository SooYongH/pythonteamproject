#클래스 정의(선언)시 필드를 미리 추가 후, 인스턴스 생성 후 수정
#인스턴스에 공통적인 필드가 있을 땐 정의 시 필드 추가하는 것이 더 편리
class Car:
    color=''
    speed=0

car1=Car()
car2=Car()

#필드 사용: 객체명(인스턴트명).필드명
print(car1.color)
print(car2.speed)

car1.color='red'
print(car1.color)
