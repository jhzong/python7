# 조건문 if
# a=100
# if a>10: # T/F
#     print("참입니다.")

# a=100
# if a>10:
#     print("참입니다.")
# else:
#     print("거짓입니다.")

# n=int(input("enter a number>> "))
# if n>=0:
#     print("양수입니다.")
# else:
#     print("음수입니다.")

# 입력된 숫자에 50을 더해서 100 보다 큰수인지 출력
# n=int(input("숫자를 입력하시오.>>"))
# n=n+50
# if n>=100:
#     print("입력값 : ",n-50,"현재값 : ",n,"100보다 큽니다.")
#     print("입력값 : %d, 현재값 : %d, %s"%(n-50, n, "100보다 크다."))
# else:
#     print("입력값 : ",n-50,"현재값 : ",n,"100보다 작습니다.")
#     print("입력값 : %d, 현재값 : %d, %s"%(n-50, n, "100보다 작다."))

#입력값의 홀짝을 출력
# n=int(input("숫자를 입력하시오."))

# if n%2==0:
#     print("입력값 : %d, 짝수"%n)
# else:
#     print("입력값 : %d, 홀수"%n)
    
# 문자열 연산자
# 문자열 슬라이싱
str1="안녕하세요"
# 안(0)녕(1)하(2)세(3)요(4)
print(str1[0])
print(str1[1])
print(str1[2])
print(str1[3])
print(str1[4])
# 안(-5)녕(-4)하(-3)세(-2)요(-1)
print(str1[-1])
print(str1[-2])
print(str1[-3])
print(str1[-4])
print(str1[-5])
print(str1[1:3]) #녕하
print(str1[1:4]) #녕하세
print(str1[1:])  #녕하세요
print(str1[:3])
print(str1[:])
# [처음번호:끝번호:스탭(증가)]
print(str1[::1])
print(str1[::-1])
print(str1[1::3])
a="123456789"
print(a[::2])
print(a[1::2])
# 3의 배수 출력
print(a[2::3])

### 입력받은 마지막 글자 출력
input1=input("파일 이름을 입력")
print("마지막 글자 : ",input1[-3:])
# 파일.'hwp'

