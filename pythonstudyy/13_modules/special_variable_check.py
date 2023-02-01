import special_variable as sv

names=[]
for i in range(5):
    sv.set_name()
    names.append(sv.get_name())

for name in names:
    print(name,end=' ')
print()