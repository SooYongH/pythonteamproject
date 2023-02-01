#텍스트파일 읽기: read()

#1. 파일열기모드로 파일객체 생성
# f=open('data/study.txt', 'r', encoding='utf=8')
#인코딩_영어가 아니라 한글인 경우 파일 형식도 추가해줘야됨
f=open('data/study_Anssi.txt', 'r')
#인코딩_한글 내용은 기본적으로 파일 형식을 anssi 코드로 인식하기 때문에 안씨로 저장한경우 추가하지 않아도 됨

#2. 파일 읽기
text=f.read()
#read(): 1개의 문자열로 전체 내용을 읽어옴
print(text)

#3. 파일 닫기
f.close()