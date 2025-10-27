# 주민번호를 입력받아, 나이를 출력
# 990101-1111111
# 000101-3111111


jumin=input("주민번호를 입력")
year=int(jumin[0:2])

# 날짜 불러오기
import datetime
now = datetime.datetime.now()

c_year=now.year
b_month=int(jumin[0:2])

if int(jumin[7])==1 or int(jumin[7])==2:
    print(c_year-(1900+b_month))
else:
    print(c_year-(2000+b_month))



# print("age : %d"%age)



