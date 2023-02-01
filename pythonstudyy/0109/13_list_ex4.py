# 학생 점수 입력받아 총점과 평균구하고 80점이상인 학생 수 출력
# 학생 점수를 내림차순으로 정렬하여 출력

data = []
total = 0
cnt = 0
n = int(input('학생수는? '))
for i in range(n):
    data.append(int(input(f'학생{i+1} 점수입력: ')))
    total += data[i]
    if data[i] >= 80:
        cnt += 1

print(f'총점 : {total}')
print(f'평균 : {total/n:.2f}')
print(f'80점이상 학생 : {cnt}명')

# data.sort(reverse=True)
print(f'점수 내림차순으로 정렬: {sorted(data, reverse=True)}')
print(data)