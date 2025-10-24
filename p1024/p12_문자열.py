#주민번호를 입력받아, 태어난 달을 출력하시오.

jumin=input("주민번호를 입력하시오. ")
#jumin="990301-3111111"
print("%s월 %s일 생입니다." % (jumin[2:4], jumin[4:6]))

#주민번호가 제대로 입력되었는지 확인하시오.
#주민번호가 14자리인지 7번자리 숫자가 1-8까지의 숫자인지 확인

#1+2번
if((len(jumin)==14) and (1<=(int(jumin[7]))<=8)): # (int(jumin[7])>=1) and (int(jumin[7])<=8)라고 쓰는게 좋다.
    print("주민번호를 제대로 입력하셨습니다.")
else:
    print("주민번호를 잘못 입력하셨습니다.")

### 풀이###
# #1번
# if(len(jumin)==14):
#     print("valid")
# else:
#     print("invalid")

# #2번
# if((int(jumin[7])>=1) and (int(jumin[7])<=8)): #파이썬에서는 1<=int(jumin[7])<=8로 표기 가능
#     print("valid")
# else:
#     print("invalid")

