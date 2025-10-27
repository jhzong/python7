# 숫자 2개를 받아 사칙연산 결과를 출력.
#% print 활용

a=int(input("type a : "))
b=int(input("type b : "))

# print("%d"%(a+b))
# print("%d"%(a-b))
# print("%d"%(a*b))
# print("%f"%(a/b))

print("%d + %d = %d"% (a,b,a+b))
print("%d - %d = %d"% (a,b,a-b))
print("%d * %d = %d"% (a,b,a*b))
print("%d / %d = %f"% (a,b,a/b))

# a=input("type a : ")
# b=input("type b : ")
# print("%d"%(int(a)+int(b)))
# print("%d"%(int(a)-int(b)))
# print("%d"%(int(a)*int(b)))
# print("%f"%float(int(a)/int(b)))
