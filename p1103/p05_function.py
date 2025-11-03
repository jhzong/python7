def cal(a,b):
    print("[basic operation]")
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

# 2 num 
# 무한 반복
# 0 terminate
# def cal(a,b):
#             print("Add",a+b)
#             print("Sub",a-b)
#             print("Mlt",a*b)
#             print("Div",a/b)
# i=0
# a_list=[0,0]
# while True:
#     print("[사칙연산]")
#     print("1.start")
#     print("0.end")
#     a=int(input("type>>"))
#     if a==1:
#         print("두수를 입력하시오.")
#         a=input("enter a number>>")
#         if a.isdigit():
#             a=int(a)
#             i+=1
#         else:
#             print("not a number")
        
#         if i ==2:
#             break
#         cal(a_list[0],a_list[1])
    
#     elif a==0:
#         print("end program")
#         break

# def kor_hello(a):
#     print("[repeat]")
#     for i in range(a):
#         print("안녕하세요.")    

# kor_hello(10)

# kor_hello(7)

# kor_hello(5)


while True:
    a=int(input("for a>>"))
    if a==0:
        print("end program")
        break
    b=int(input("for b>>"))
    cal(a,b)
    
    
    
    