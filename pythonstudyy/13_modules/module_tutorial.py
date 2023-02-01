
# 모듈 전체 참조
# import 모듈명(=파일명) (as 별칭)
import module1

#모듈 내 일부만 참조
# from 모듈명 import 변수명 or 함수명 (as 별칭)
# from 모듈명 import *
# ('__로 시작하는 스페셜 변수나 매직 메서드를 제외한 모든 것 참조')
# from module1 import *

#모듈이 동일한 파일 내에 없으면 경로를 따로 불러줘야 한다.


# 호출 형식 : 모듈명.함수명
module1.func1()
module1.func2()
module1.func3()

#import date, datetime
#import pickle 객체 저장 및 사용 모듈
#import sys/os 시스템 모듈

