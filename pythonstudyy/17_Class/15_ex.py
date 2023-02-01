#보통 메서드 함수 괄호 안에 필드(속성)이 들어감
# 메서드 함수 다음줄부터 필드(속성) 지정,추가 및 수정함

class Dog:
    count=0
    def __init__(self,name,breed,size,age,color):
        self.name=name  #필드(속성)
        self.__breed=breed
        self.size=size
        self.age=age
        self.color=color
        Dog.count+=1
        print(str(Dog.count)+'마리가 태어났습니다.')

    def eat(self,food): #메서드 함수
        self.food=food
        print(f'{self.name}이(가) {self.food}를 먹는다') #food를 매개변수로

    def sleep(self):
        print(f'{self.name}이 잠잔다')

    def sit(self):
        print(f'{self.name}이 앉아있다')

    def run(self):
        print(f'{self.name}이 뛴다')

    def __str__(self): #숫자를 문자열로 바꿔 프린트 #retr은 문자열 형태로 프린트
        return f'{self.name}의 나이는 {self.age}살 품종은 {self.__breed}입니다'
    #print말고 return

    def __lt__(self, other): ##이게 트루면
        # if self.age < other.age :
        #     print(f'{self.name}은 {other.name}보다 어립니다')
        # else:
        #     print(f'{self.name}은 {other.name}보다 나이가 많습니다')
        return self.age < other.age ##반환해라

    def __eq__(self, other):
        # if self.age == other.age :
        #     print(f'두 마리 모두 {self.age}살 입니다')
        # else:
        #     print(f'{self.name}은 {self.age}살 {other.name}은 {other.age}살 입니다')
        return self.age == other.age



dog1=Dog('삐삐','Maltese','small',2,'white')
dog2=Dog('벤','Chow Chow','medium',3,'brown')
dog3=Dog('뭉치','Mastiff','large',5,'black')

print(dog1)
print(dog2)
print(dog3)

print(dog1<dog2) # print(dog1,dog2) 오류


print(dog1.eat('한우'))
print(dog2.sleep())
print(dog3.run())

print(Dog.count)
