# 튜플 연산 : 치환

(x1, y1), (x2, y2) = (1,2), (3,4)
print(x1, y1)
print(x2, y2)

a, b = 10, 15
print(a,b)

# 패킹(packing) : 한 데이터에 여러 데이터를 넣는 것
t = 1, 2, 'hello'
print(t)

# 언패킹(unpacking) : 한 데이터에서 데이터를 각각 꺼내오는 것
x, y, z = t
print(x,y,z)

#
t2 = 1,2,3,4,5
a, *b = t2
print(a, b)

*a, b = t2
print(a, b)

a, b, *c = t2
print(a,b,c)

a, *b, c = t2
print(a,b,c)

# a, b, c = t2
# print(a,b,c)

# a, *b, *c = t2
# print(a,b,c)

#* : 여러개

