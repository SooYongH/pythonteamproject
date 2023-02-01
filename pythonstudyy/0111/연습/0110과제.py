std1={'이름':'홍길동','국어':87,'영어':98, '수학':100,'과학':90}
std2={'이름':'이몽룡','국어':92,'영어':98, '수학':96,'과학':98}
std3={'이름':'성춘향','국어':72,'영어':80, '수학':87,'과학':65}
std4={'이름':'변학도','국어':50,'영어':70, '수학':90,'과학':50}
std5={'이름':'월매','국어':100,'영어':90,'수학':50,'과학':80}

students=[std1,std2,std3,std4,std5]
print('이름  국어 영어 수학 과학')

for std in students :
    for key in std.keys():
        print(std[key], end= ' ')
    print()
print('----------')
for std in students :
    # total=std['국어']+std['영어']+std['수학']+std['과학']
    total=0
    for key in std.keys():
        if key=='이름':
            continue
        else:
            total+=std[key]
    avg=total/4
    print(f'{std["이름"]} {total} {avg:.1f}')
