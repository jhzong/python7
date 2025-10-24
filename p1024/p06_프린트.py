# print("%d" % (100,200)) error
# print("%d %d" % 100) error
# print("%d %d" % (100,200))


# str1="이름"
# str2="국어"
# str3="영어"
# str4="수학"
# str5="합계"
# str6="평균"
# print(str1,str2,str3,str4,str5,str6)
# \t 탭 \n 줄바꿈

name=input("이름을 입력하시오. ")
kor=int(input("국어 점수 :"))
eng=int(input("영어 점수 :"))
math=int(input("수학 점수 :"))
total=kor+eng+math
avg=total/3


print("-"*50)
print("%s\t%s\t%s\t%s\t%s\t%s" % ("이름","국어","영어","수학","합계","평균"))
print("-"*50)
print("%s\t%d\t%d\t%d\t%d\t%.2f" % (name,kor,eng,math,total,avg))