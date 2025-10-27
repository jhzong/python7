# stu_data=[] #리스트
# stu_data.append(1)
# stu_data.append("홍길동")
# stu_data.append(100)
# stu_data.append(100)
# stu_data.append(100)
# print(stu_data)

stu_datas=[]

name1=input("name : ")
kor1=int(input("Korean score : "))
eng1=int(input("English score : "))
mth1=int(input("Math score : "))
total1=kor1+eng1+mth1
avg1=total1/3
stu_data1=[name1,kor1,eng1,mth1,total1,avg1]
stu_datas.append(stu_data1)

name2=input("name : ")
kor2=int(input("Korean score : "))
eng2=int(input("English score : "))
mth2=int(input("Math score : "))
total2=kor2+eng2+mth2
avg2=total2/3
stu_data2=[name2,kor2,eng2,mth2,total2,avg2]
stu_datas.append(stu_data2)

print("-"*50)
print(stu_datas)