class Car:
    pass

#인스턴스를 생성한 후 (커스터마이징 이름)
car1=Car()
car2=Car()
#필드 추가 : :~~~ (커스터마이징 내용 정하기)
# 필드 추가 후 사용 (커스터마이징 내용 디폴트 디자인에 접목시키기)
car1.color='red'
car2.color='blue'
car1.speed=0
car2.speed=100
print(car1.color)
print(car2.speed)
#.은 소속 소유를 뜻함

#1. 클래스가 왜 필요한가?
# 코드의 중복, 재사용, 유지보수 용이함
# 기존의 구조적 프로그래밍 : 함수 위주로 코드 작성
# 수정할 때 수정영역을 축소할 수 있음
# 함수와 변수를 같이 묶어서 코딩 => 객체 (객체지향 프로그래밍 Object Oriented Programming: OOP)
# 함수 + 변수 => 객체 => 클래스
# 클래스 : 설계도 (ex.개)
# 인스턴스(객체): 실존 (메모리) (ex.비숑, 시츄~~)

#2. 클래스 구현
# 1단계 : 클래스 선언(정의)
#     class 클래스명 :
#         필드 정의(생성자)
#         매서드들 정의
# 2단계 : 인스턴스 생성(호출)
#     인스턴스명=클래스명() <=생성자
#     mycar=Car()
# 3단계 : 필드나 메서드 사용
#     인스턴스명.필드=값 (수정)
#     인스턴스명.필드 (이용)
#     인스턴스명.메서드()

#3. 클래스 선언 형식
# 방식1 인스턴스 생성 후 필드 추가
#  인스턴스명.필드명=값
# class 클래스명:
#     pass

# 클래스 선언시 필드 추가
# class 클래스명:
#     필드=값


# class 클래스명:
#     def 메서드명(self,*args):

# 메서드는 함수 정의와 동일 카멜케이스 지향
#
# 메서드 중 특이한 메서드 : 생성자
# 인스턴스를 생성하고 필드값 초기화
#
# 생성자 이름은 __init__(self.*args)
#
# self키워드 의미? 인스턴스 자신을 나타냄

#4 필드를 접근하기 위한 메서드들
# -필드의 값을 가져오기 위한 메서드 : get필드명()
# -필드에 값을 지정(변경)하기 위한 메서드 : set필드명()
# (비공개필드 접근에 유용)

#5 비공개필드: __필드명
# => 클래스 내부에서만 접근 가능
# 인스턴트 생성한 후 직접 필드명 사용하여 접근불가
# 클래스 내부에서 접근 가능한 메서드를 정의해서 사용

#6 비공개메서드: __메서드명()
# =>클래서 내부에서만 접근 가능
# 다른 메서드에서 이 메서드를 사용하도록 정의

#7 특별한 메서드들
# __str__(),__del__(),~~

#8클래스 변수와 인스턴스 변수
# -인스턴스 변수 : 생성자 안에서 사용
# 자신의 인스턴스 내에서만 사용(유효범위)
# 인스턴스이름.변수
#
# -클래스 변수 : 모든 인스턴스에서 공통으로 공유하여 사용
# 클래스 내에서 전역변수처럼 정의하여 사용
# 클래스이름.변수

#9 상속
# class 자식클래스(부모클래스)
#     pass
# 메소드 재정의(오버라이딩 overriding)
#
#10 다형성과 가시성
# 장식(데코레이터)@property

#11 포함관계(has a)와 상속관계(is a)

#12 다중상속
# mro() : 동일한 이름의 메소드를 상속받을 때 호출되는 순서

#13 정적메서드, 클래스메서드
# 클래스명.메서드이름()
# 정적메서드 : 함수처럼 사용 (self 키워드가 없이)
# @staticmethod
#
# 클래스메서드 : 클래스변수나 클레서 메서드를 사용할 때
# @classmethod (self 대신 cls로)