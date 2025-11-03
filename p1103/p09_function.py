# 입력한 글자를 입력한 숫자만큼 반복
# 안녕하세요 3

# str1=input("type>>")
# num=int(input("reteat>>"))
# for i in range(num):
#     print(str1)

# def s_print(str1,num):
#     for i in range(num):
#         print(str1)
# str1=input("type>>")
# num=int(input("reteat>>"))
# s_print(str1,num)        


# 함수를 사용하여 cal(3개)
# 두수와 +-*/중 1개를 입력받아
# 결과를 출력

# 10
# 2
# +
# 10+2=12


# def cal(num1,num2,str1):
#     if str1=='+':
#         print(num1+num2)
#     elif str1=='-':    
#         print(num1-num2)
#     elif str1=='*':    
#         print(num1*num2)
#     elif str1=='/':    
#         print(num1/num2)

# num1=int(input("num>>"))
# num2=int(input("num>>"))
# str1=input("type>>")
# cal(num1,num2,str1)

# def cal(a,b):
#     print(a+b)

# a=int(input("enter number>>"))
# b=int(input("enter number>>"))
# cal(a,b)


# def cal(a,b):
#     for i in range(b-a):
#         a+=i
#         print(a)
        
# a=int(input("enter number>>"))
# b=int(input("enter number>>"))
# cal(a,b)

# a,b를 입력받아 a~b까지의 합
# for i in range(a,b+1):
#     sum+=i
# print(sum)

def cal(a,b):
    sum=0
    for i in range(a,b+1):
        sum+=i
    print(sum)

a=int(input("enter number>>"))
b=int(input("enter number>>"))
cal(a,b)


