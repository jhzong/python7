# 국, 영, 수 점수를 입력 받아 함계, 평균을 출력

#\t:탭키 간격벌리기, \n:줄바꿈
# print("안녕\t하\n세요.")

name=input("이름 : ")
kor=int(input("국어 점수 : "))
eng=int(input("영어 점수 : "))
math=int(input("수학 점수 : "))
sum=kor+eng+math
avg=sum/3
# print("합계는 %d입니다."%sum)
# print("평균은 %.2f입니다."%avg)

name1=input("이름 : ")
kor1=int(input("국어 점수 : "))
eng1=int(input("영어 점수 : "))
math1=int(input("수학 점수 : "))
sum1=kor1+eng1+math1
avg1=sum1/3

name2=input("이름 : ")
kor2=int(input("국어 점수 : "))
eng2=int(input("영어 점수 : "))
math2=int(input("수학 점수 : "))
sum2=kor2+eng2+math2
avg2=sum2/3

print(" "*15+"학생성적프로그램")
print("-"*50)
print("이름\t국어\t영어\t수학\t합계\t평균")
print("-"*50)
print("%s\t%d\t%d\t%d\t%d\t%.2f"%(name,kor,eng,math,sum,avg))
print("%s\t%d\t%d\t%d\t%d\t%.2f"%(name1,kor1,eng1,math1,sum1,avg1))
print("%s\t%d\t%d\t%d\t%d\t%.2f"%(name2,kor2,eng2,math2,sum2,avg2))