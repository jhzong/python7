import random

title=['num','name','Korean','English','Math','Sum','Average']
stu_info=[]
num=10101

# 입력 파트
# 이름/국/영/수 입력 > 입력된 성적으로 합계/평균 계산 > 데이터를 리스트(stu_info)에 입력
print('<<INPUT DATA>>')
print('inputing data : student number {}'.format(num))
name=input('input name>>')
kor=int(input('input Korean score>>'))
eng=int(input('input English score>>'))
math=int(input('input Math score>>'))
sum=kor+eng+math
avg=sum/3
stu_info.append([num,name,kor,eng,math,sum,avg])
num=num+1
print('[input complete]')

print(stu_info)

# 출력
# 입력된 성적을 리스트의 형태로 정렬해 출력
print('TEST SCOREBOARD')
print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(title))
for i in stu_info:
    print('{}\t{}\t{}\t{}\t{}\t{}\t{}'.format(i))

# 수정
# 국/영/수 중 데이터를 수정 > 수정된 값에 따라 합계/평균도 변경
print('SCORE EDITOR')
print('{}.\t{}\t{}'.format('idx','no.','name'))
for idx, s in enumerate(stu_info):
    print('{}.\t{}\t{}'.format(idx, s))
e=int(input('select student>>'))

print('Korean(1) English(2) Math(3)')
sbj=int(input('select subject>>'))

print("{}'s current {} score : {}".format(stu_info[e-1][1],title[sbj+1],stu_info[e-1][sbj+1]))
n_score=int(input('input new score>>'))

stu_info[e-1][sbj+1]=n_score
stu_info[e-1][5]=stu_info[e-1][2]+stu_info[e-1][3]+stu_info[e-1][4]
stu_info[e-1][6]=stu_info[e-1][5]/3

# 삭제
# 리스트에서 학생 데이터를 지정해 삭제
print()


# 종료
