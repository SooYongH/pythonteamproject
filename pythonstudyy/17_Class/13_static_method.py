#정적 메서드 static method
#@staticmethod 키워드를 매서드 앞에 지정하여 순수함수를 만듦

class Calc:
    @staticmethod
    def add(a,b): #self 없어야됨
        print(f'{a}+{b}={a+b}')

    @staticmethod
    def mul(a,b):
        print(f'{a}*{b}={a*b}')

#클래스에서 바로 메서드 호출
Calc.add(10,5)
Calc.mul(10,4)