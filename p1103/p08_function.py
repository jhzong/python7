# # 매개변수의 개수는 호출하는 변수의 개수와 동일해야함.
# # 매개변수의 타입은 호출하는 타입과 일치해야함.
# def add(a,b):
#     return a+b

# a=add(1,2)
# print(a)

# # 가변 매개변수
# def add(a,b,*c): # 변수 앞에 *을 붙이면 가변 매개변수가 됨.
#     sum=a+b
#     for i in c:  # c: 여러개 가능
#         sum+=i
#     return sum

# print(add(1,2,3))


#

# def print_str(a,b,*c):
#     print(a)
#     print(b)
#     for i in c:
#         print(i)
        
# print_str("안녕","사과","홍길동","점수",100)

# def print_str(*c):
#     for i in c:
#         print(i)
        
# print_str("안녕","사과",100)


# 여러개를 입력받아, 함수를 이용해 출력
# c=[]
# while True:
#     def print_str(*c):
#         for i in c:
#             print(i)
            
# 5번 입력받아, 0을 입력하면 모두 출력되도록 구성하시오
    # exe=input("type 0 to excute>>")
    # c.append(exe)


# str1=[0,0,0,0,0]

# for i in range(5):
#     str1[i]=input("type anything>>")
    
# print(*str1)


# 
stus=[1,"Hong",100,90,80]

# kor, eng, math 점수를 입력받아, return을 적용
def sum(kor,eng,math):
    
    return kor+eng+math

stus.append(sum(stus[2],stus[3],stus[4]))
print(stus)

def avg(kor,eng,math):
    
    return (kor+eng+math)/3

stus.append(avg(stus[2],stus[3],stus[4]))
print(stus)
