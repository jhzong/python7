# 3개의 값을 받아, 숫자를 모두 합친 금액을 출력
# 1000원 이상 입력하세오.
# m1=int(input("금액을 입력하시오>>"))
# m2=int(input("금액을 입력하시오>>"))
# m3=int(input("금액을 입력하시오>>"))
# sum=m1+m2+m3
# # print("총금액 {:,d}원".format(sum))
# print("1번금액 : {:,d}원\n2번금액 : {:,d}원\n3번금액 : {:,d}원\n총금액 : {:,d}원".format(m1,m2,m3,sum))

# 총금액 1,000,000원

# year=2025
# month=10
# day=28
# print("%d년 %d월 %d일"%(year,month,day))
# date_format="{}년 {}월 {}일".format(year,month,day)
# print(date_format)

# type and print Hong, Kor, Eng, Math, Sum, Avg
a_list=["Hong",100,90,80,270,90.0]
print("name:{}, Kor:{}, Eng:{}, Math:{}, Sum:{}, Avg:{:.2f}".\
    format(a_list[0],a_list[1],a_list[2],a_list[3],a_list[4],a_list[5]))
print("name:{}, Kor:{}, Eng:{}, Math:{}, Sum:{}, Avg:{:.2f}".format(*a_list))


name=input('type name>>')
kor=int(input('enter Kor score>>'))
eng=int(input('enter Eng score>>'))
math=int(input('enter Math score>>'))
sum=kor+eng+math
avg=sum
print('name:{}, Kor.S:{}, Eng.S:{}, Math.S:{}, Sum:{}, Avg:{:.2f}'.format(name,kor,eng,math,sum,avg))


