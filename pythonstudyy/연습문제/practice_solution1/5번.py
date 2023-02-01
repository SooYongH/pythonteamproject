#방법1
for i in range(1,6):
    print(' '*(5-i) + '*'*(2i-1))

# #방법2
# n='*'
# for i in range(1,6):
#     for j in range(5-i):
#         print(end=' ')
#     for j in range(1,2*i):
#         print(n,end='')
#     print()