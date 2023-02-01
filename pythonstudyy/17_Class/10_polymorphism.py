#다형성(polymorphism)

class Animal:
    def __init__(self,type,name):
        self.type=type
        self.name=name

    def talk(self):
        raise NotImplementedError('Subclass must implement abstract method')
    #구체적으로 정의하지 않고 상속받은 곳 내에서 각각 알아서 실행해라

class Cat(Animal):
    def talk(self):
        return 'Meow'

class Dog(Animal):
    def talk(self):
        return 'woof woof'

cat1=Cat('러시아','냐옹이')
cat2=Cat('페르시아','나비')

dog=Dog('비숑','앵두')

print(dog.talk())

animals=[cat1,cat2,dog]
for animal in animals:
    print(animal.name,':',animal.talk())
    #name은 필드 talk은 메서드
