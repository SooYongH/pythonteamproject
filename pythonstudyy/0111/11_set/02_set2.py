# set연산 : 교집합, 합집합, 차집합

# 합집합 : A | B  or  A.union(B)
# 교집합 : A & B  or A.intersection(B)
# 차집합 : A - B or A.difference(B)

A = {1,2,3}
B = {3,4,5}

#합집합
C= A | B
print(C)
C= A.union(B)
print(C)

#교집합
C= A & B
print(C)
C= A.intersection(B)
print(C)

# 차집합
C = A-B
print(C)
C = A.difference(B)
print(C)

D = B-A
print(D)
D = B.difference(A)
print(D)

