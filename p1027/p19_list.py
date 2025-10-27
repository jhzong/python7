# 이름,국어,영어,수학,합계,평균
# 학생 3명의 성적입력해 출력
## 개별 변수 입력해 

stus=[]

stu=[]
name=input("name : ")
stu.append(name)
kor=int(input("Korean score : "))
stu.append(kor)
eng=int(input("English score : "))
stu.append(eng)
mth=int(input("Math score : "))
stu.append(mth)
total=kor+eng+mth
stu.append(total)
avg=total/3
stu.append(avg)

stus.append(stu)
print(stus)

stu=[]
name=input("name : ")
stu.append(name)
kor=int(input("Korean score : "))
stu.append(kor)
eng=int(input("English score : "))
stu.append(eng)
mth=int(input("Math score : "))
stu.append(mth)
total=kor+eng+mth
stu.append(total)
avg=total/3
stu.append(avg)

stus.append(stu)
print(stus)

stu=[]
name=input("name : ")
stu.append(name)
kor=int(input("Korean score : "))
stu.append(kor)
eng=int(input("English score : "))
stu.append(eng)
mth=int(input("Math score : "))
stu.append(mth)
total=kor+eng+mth
stu.append(total)
avg=total/3
stu.append(avg)

stus.append(stu)
print(stus)

print(stus[0])
print(stus[0][0])