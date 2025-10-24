# 이름 입력 str %s
# 국어 점수 int
# 영어 점수 int
# 수학 점수 int
# 합계 int %d
# 평균 float %f

name=input("이름을 입력하시오. ")
kor=int(input("국어 점수를 입력하시오. "))
eng=int(input("영어 점수를 입력하시오. "))
math=int(input("수학 점수를 입력하시오. "))
sum=kor+eng+math
avg=sum/3 


print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,sum,avg))# \t : 공백(4칸)


