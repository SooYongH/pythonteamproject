#파이썬의 객체를 저장&읽기
import pickle

f=open('data/list.pickle','wb')
test_list=[1,2,3,4,5,6]
pickle.dump(test_list,f) #test_list를 f에다가 쓴다
f.close()

f=open('data/list.pickle','rb')
read=pickle.load(f)
print(read)
print(type(read))

read.append(100)
print(read)
f.close()