
# twos=set((lambda x : x)(i) for i in range(2,501,2))
# threes=set((lambda x : x)(i) for i in range(3,501,3))

twos={x for x in range(2,501,2)}
threes={i for i in range(3,501,3)}

two_three=twos.union(threes)
# print(two_three)
print(len(two_three))