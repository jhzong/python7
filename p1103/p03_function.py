# 함수 : 특정명령어 실행. 반복을 제거하고, 유지보수에 유리, 코드양을 대폭 줄일수있다.
# print() 함수

# 함수의 형태
# def 함수명():
#     pass

# 함수호출
# 함수명()

def calculate(a,b): # 함수정의
    print("더하기",a+b)
    print("빼기",a-b)
    print("곱하기",a*b)
    print("나누기",a/b)

a,b=10,2
calculate(10,2) # 함수호출 - 정의된 함수를 불러옴
a,b=5,3
calculate(5,3)
a,b=2,1
calculate(2,1)



# a,b=10,2
# print("plus :",a+b)
# print("minus :",a-b)
# print("multi :",a*b)
# print("divid :",a/b)

# a,b=5,3
# print("plus :",a+b)
# print("minus :",a-b)
# print("multi :",a*b)
# print("divid :",a/b)