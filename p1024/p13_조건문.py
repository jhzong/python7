# if문은 꼭':'으로 닫아줘야 함.
# 아래 문구는 꼭 들여쓰기 해야 함.
# if (10>5):
#     print("정상입니다.")
# else:
#     print("비정상입니다.")


# 숫자를 입력받아 100보더 큰수인지 아닌지 출력

# num = int(input("숫자를 입력하시오. "))
# if(num<100):
#     print("100보다 작습니다.")
# else:
#     print("100보다 큽니다.")


# 입력된 숫자가 짝수인지 홀수인지 출력
# num%2==0

# num=int(input("숫자를 입력"))
# if(num%2 == 0):
#     print("짝")
# else:
#     print("홀")
    
    
# 내부모듈 - 외우기
import datetime
now = datetime.datetime.now()
print(now)

print(now.year,"년")
print(now.month,"월")
print(now.day,"일")
print(now.hour,"시")
print(now.minute,"분")
print(now.second,"초")



# 입력한 주민번호의 생월과 현재 날짜와 같은 월이면
# 이벤트 대상입니다. 아닙니다.
jumin=input("주민번호를 입력하시오. ")
if(int(jumin[2:4])==now.month):
    print("이벤트 대상입니다.")
else:
    print("이벤트 대상이 아닙니다.")



# n="03"
# print(int(n))
# n=3
# print("%02d" % n)

#[시작번호:끝번호:스탭]
str1="abcdefg"
print(str1[1:6:2])  # bdf
print(str1[:5])     # abcd
print(str1[5:2:-1]) # fed
print(str1[::-1])   # gfedcba

