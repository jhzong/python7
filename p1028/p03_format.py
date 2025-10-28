# year=2025
# month=10
# day=28
# # 년 월 일 출력
# print("%d년 %d월 %d일"%(year,month,day))# print 출력만 되지 저장이 안됨.
# ## format() 함수
# date1="{:d}년 {:d}월 {:d}일".format(year,month,day)#{}안의 :x는 생략가능.
# print(date1)

# # %print
# a=10
# print("%5d"%a)
# print("%05d"%a)

# b=10.2345678
# print("%f"%b)
# print("%.2f"%b)
# print("%7.2f"%b)
# print("%07.2f"%b)

a=10
a_format="{}".format(a)
a_format1="{:10d}".format(a)   # 10자리 확보
a_format2="{:010d}".format(a)  # 공백 0으로 채움
a_format3="{:010,d}".format(a) # 천단위 ","로 표시
print(a_format)
print(a_format1)
print(a_format2)
print(a_format3)

b=25.2345678
b_format="{}".format(b)
b_format1="{:.2f}".format(b)
b_format2="{:8.2f}".format(b)
b_format3="{:08.2f}".format(b)
print(b_format)
print(b_format1)
print(b_format2)
print(b_format3)

# list 타입 format 함수 활용
stus=['Hong',100,90,80]
print("name : {}, Kor : {}, Eng : {}, Math : {}".\
    format(stus[0],stus[1],stus[2],stus[3]))
# *stus -> 전개연산자 stus[x](x:0-3)
print("name : {}, Kor : {}, Eng : {}, Math : {}".format(*stus))


###
bank=[1,"Hong",100000]
# print no.1 Hong 100,000won
# use format()
print("no.{} {} {:,d}won".format(*bank))


name="You"
rank=3
result=98.234567
## name:You, rank:3, result:98.23%
profile=[name,rank,result]
print("name : {}, rank : {}, S_rate : {:.2f}%".format(name,rank,result))
print("name : {}, rank : {}, S_rate : {:.2f}%".format(*profile))
## f함수
print(f"name : {name}, rank : {rank}, S_rate : {result:.2f}%")


