# a를 소수점 2자리까지 출력
a=758.12345678
print("%.2f"%a)

# b를 10공간 확보해 0으로 채우고 소수점 1자리까지 출력
b=25.05
print("%010.1f"%b)

# c를 정수 실수 문자열로 출력
c=150.15
print("%f"%c) # print(c)
print("%d"%c) # c1=int(c) -> print(c1)
print("%s"%c) # c2=str(c) -> print(c2)

# d를 20번 출력
d="*"
print(d*20)