# 예제. 파티에 참석한 사람들의 정보를 set으로 구성하여 연산
# partyA : 'Park', 'Kim', 'Lee'
# partyB : 'Park', 'hong', 'Kang'

partyA = {'Park', 'Kim', 'Lee'}
partyB = {'Park', 'hong', 'Kang'}
print('partyA:',partyA)
print('partyB',partyB)
# 두 파티에 모두 참석한 사람은?
print(partyA & partyB)
print(partyA.intersection(partyB))

# 파티에 참석한 사람은?
print(partyA | partyB)
print(partyA.union(partyB))

# 파티A에만 참석한 사람은?
print(partyA - partyB)
print(partyA.difference(partyB))

# 파티B에만 참석한 사람은?
print(partyB - partyA)
print(partyB.difference(partyA))
