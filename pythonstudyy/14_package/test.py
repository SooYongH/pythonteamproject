#방법1 전체 호출
# import mypack.pack1.module11 as p11
# p11.func11()

#방법2 일부 함수 호출
# from mypack.pack1.module11 import func11
# func11()

#방법3 매직 키워드 제외하고 호출
from mypack.pack1.module11 import *
func11()